import streamlit as st
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.graph_objects as go
import plotly.express as px

# Download required NLTK data
@st.cache_resource
def download_nltk_data():
    try:
        nltk.download('vader_lexicon', quiet=True)
    except:
        pass

download_nltk_data()

# Load RoBERTa model
@st.cache_resource
def load_roberta_model():
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    return tokenizer, model

# Initialize VADER
@st.cache_resource
def load_vader():
    return SentimentIntensityAnalyzer()

def analyze_sentiment_vader(text, sia):
    """Analyze sentiment using VADER"""
    scores = sia.polarity_scores(text)
    return scores

def analyze_sentiment_roberta(text, tokenizer, model):
    """Analyze sentiment using RoBERTa"""
    encoded_text = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    return {
        'negative': scores[0],
        'neutral': scores[1],
        'positive': scores[2]
    }

def create_sentiment_chart(vader_scores, roberta_scores):
    """Create a comparison chart for both models"""
    fig = go.Figure()
    
    # VADER scores
    fig.add_trace(go.Bar(
        name='VADER',
        x=['Negative', 'Neutral', 'Positive'],
        y=[vader_scores['neg'], vader_scores['neu'], vader_scores['pos']],
        marker_color='lightblue'
    ))
    
    # RoBERTa scores
    fig.add_trace(go.Bar(
        name='RoBERTa',
        x=['Negative', 'Neutral', 'Positive'],
        y=[roberta_scores['negative'], roberta_scores['neutral'], roberta_scores['positive']],
        marker_color='salmon'
    ))
    
    fig.update_layout(
        title='Sentiment Analysis Comparison',
        xaxis_title='Sentiment',
        yaxis_title='Score',
        barmode='group',
        height=400
    )
    
    return fig

def get_sentiment_label(scores, model_type='vader'):
    """Determine overall sentiment label"""
    if model_type == 'vader':
        compound = scores['compound']
        if compound >= 0.05:
            return '😊 Positive', 'success'
        elif compound <= -0.05:
            return '😞 Negative', 'error'
        else:
            return '😐 Neutral', 'warning'
    else:  # roberta
        max_score = max(scores['negative'], scores['neutral'], scores['positive'])
        if scores['positive'] == max_score:
            return '😊 Positive', 'success'
        elif scores['negative'] == max_score:
            return '😞 Negative', 'error'
        else:
            return '😐 Neutral', 'warning'

# Streamlit App
st.set_page_config(
    page_title="Real-time Review Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Real-time Review Sentiment Classifier")
st.markdown("""
This application analyzes the sentiment of product reviews in real-time using two powerful techniques:
- **VADER**: A lexicon and rule-based sentiment analysis tool
- **RoBERTa**: A transformer-based deep learning model from Hugging Face
""")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    ### How it works:
    1. Enter your review text
    2. Choose analysis model(s)
    3. Get instant sentiment scores
    
    ### Models:
    - **VADER**: Fast, interpretable, great for social media text
    - **RoBERTa**: Advanced NLP, high accuracy
    """)
    
    st.markdown("---")
    st.markdown("### Example Reviews:")
    
    examples = {
        "Positive": "This product is absolutely amazing! Best purchase I've ever made. Highly recommend!",
        "Negative": "Terrible quality. Broke within a week. Complete waste of money.",
        "Neutral": "The product arrived on time. It works as described in the specifications.",
        "Mixed": "The product quality is good but the customer service was disappointing."
    }
    
    for label, text in examples.items():
        if st.button(f"Try {label} Example"):
            st.session_state.example_text = text

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # Text input
    default_text = st.session_state.get('example_text', '')
    review_text = st.text_area(
        "Enter your review:",
        value=default_text,
        height=150,
        placeholder="Type or paste your product review here..."
    )
    
    # Model selection
    st.markdown("### Select Analysis Model:")
    col_vader, col_roberta = st.columns(2)
    with col_vader:
        use_vader = st.checkbox("VADER", value=True)
    with col_roberta:
        use_roberta = st.checkbox("RoBERTa", value=True)
    
    analyze_button = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)

with col2:
    st.markdown("### Quick Stats")
    if review_text:
        st.metric("Character Count", len(review_text))
        st.metric("Word Count", len(review_text.split()))
    else:
        st.info("Enter text to see stats")

# Analysis section
if analyze_button and review_text.strip():
    if not use_vader and not use_roberta:
        st.error("⚠️ Please select at least one analysis model!")
    else:
        with st.spinner("Analyzing sentiment..."):
            st.markdown("---")
            st.markdown("## 📈 Analysis Results")
            
            results_col1, results_col2 = st.columns(2)
            
            # VADER Analysis
            if use_vader:
                with results_col1:
                    st.markdown("### 🎯 VADER Analysis")
                    sia = load_vader()
                    vader_scores = analyze_sentiment_vader(review_text, sia)
                    
                    label, status = get_sentiment_label(vader_scores, 'vader')
                    if status == 'success':
                        st.success(f"**Overall Sentiment:** {label}")
                    elif status == 'error':
                        st.error(f"**Overall Sentiment:** {label}")
                    else:
                        st.warning(f"**Overall Sentiment:** {label}")
                    
                    st.markdown("**Detailed Scores:**")
                    st.metric("Positive", f"{vader_scores['pos']:.3f}")
                    st.metric("Neutral", f"{vader_scores['neu']:.3f}")
                    st.metric("Negative", f"{vader_scores['neg']:.3f}")
                    st.metric("Compound", f"{vader_scores['compound']:.3f}")
            
            # RoBERTa Analysis
            if use_roberta:
                with results_col2:
                    st.markdown("### 🤖 RoBERTa Analysis")
                    tokenizer, model = load_roberta_model()
                    roberta_scores = analyze_sentiment_roberta(review_text, tokenizer, model)
                    
                    label, status = get_sentiment_label(roberta_scores, 'roberta')
                    if status == 'success':
                        st.success(f"**Overall Sentiment:** {label}")
                    elif status == 'error':
                        st.error(f"**Overall Sentiment:** {label}")
                    else:
                        st.warning(f"**Overall Sentiment:** {label}")
                    
                    st.markdown("**Detailed Scores:**")
                    st.metric("Positive", f"{roberta_scores['positive']:.3f}")
                    st.metric("Neutral", f"{roberta_scores['neutral']:.3f}")
                    st.metric("Negative", f"{roberta_scores['negative']:.3f}")
            
            # Visualization
            if use_vader and use_roberta:
                st.markdown("---")
                st.markdown("### 📊 Model Comparison")
                fig = create_sentiment_chart(vader_scores, roberta_scores)
                st.plotly_chart(fig, use_container_width=True)
            elif use_vader:
                st.markdown("---")
                st.markdown("### 📊 VADER Sentiment Distribution")
                fig = go.Figure(data=[
                    go.Bar(
                        x=['Negative', 'Neutral', 'Positive'],
                        y=[vader_scores['neg'], vader_scores['neu'], vader_scores['pos']],
                        marker_color=['#FF6B6B', '#FFE66D', '#4ECDC4']
                    )
                ])
                fig.update_layout(height=400, yaxis_title='Score')
                st.plotly_chart(fig, use_container_width=True)
            elif use_roberta:
                st.markdown("---")
                st.markdown("### 📊 RoBERTa Sentiment Distribution")
                fig = go.Figure(data=[
                    go.Bar(
                        x=['Negative', 'Neutral', 'Positive'],
                        y=[roberta_scores['negative'], roberta_scores['neutral'], roberta_scores['positive']],
                        marker_color=['#FF6B6B', '#FFE66D', '#4ECDC4']
                    )
                ])
                fig.update_layout(height=400, yaxis_title='Score')
                st.plotly_chart(fig, use_container_width=True)

elif analyze_button:
    st.warning("⚠️ Please enter some text to analyze!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using Streamlit, VADER, and RoBERTa</p>
    <p>Analyze customer reviews to understand sentiment patterns and improve your products!</p>
</div>
""", unsafe_allow_html=True)