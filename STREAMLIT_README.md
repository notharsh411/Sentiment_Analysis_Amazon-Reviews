# 🎯 Real-time Review Sentiment Classifier with Streamlit

A beautiful, interactive web application for analyzing product review sentiments in real-time using VADER and RoBERTa models.

## 🚀 Quick Start

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the App

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## ✨ Features

- **Dual Model Analysis**: Compare results from both VADER and RoBERTa sentiment analysis models
- **Real-time Processing**: Instant sentiment analysis as you type
- **Interactive Visualizations**: Beautiful charts powered by Plotly
- **Example Reviews**: Pre-loaded examples to test different sentiment types
- **Detailed Metrics**: Get comprehensive sentiment scores and breakdowns
- **Modern UI**: Clean, responsive design with emojis and color-coded results

## 🎨 How to Use

1. **Enter Your Review**: Type or paste a product review in the text area
2. **Select Models**: Choose to analyze with VADER, RoBERTa, or both
3. **Click Analyze**: Get instant sentiment analysis results
4. **View Results**: See sentiment labels, detailed scores, and comparison charts

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **VADER**: Lexicon-based sentiment analysis
- **RoBERTa**: Transformer-based model from Hugging Face
- **Plotly**: Interactive visualizations
- **NLTK**: Natural language processing toolkit

## 📊 Model Information

### VADER
- Fast and efficient
- Rule-based approach
- Great for social media and short text
- Provides compound, positive, neutral, and negative scores

### RoBERTa
- Deep learning-based
- Pre-trained on Twitter data
- High accuracy for complex sentiments
- Provides positive, neutral, and negative probabilities

## 🎯 Use Cases

- Analyze customer product reviews
- Monitor social media sentiment
- Evaluate feedback and comments
- Research sentiment patterns
- Test marketing copy and messaging

## 📝 Notes

- First run may take a few moments to download the RoBERTa model
- The app caches models for faster subsequent analyses
- Supports text up to 512 tokens for RoBERTa model

---

Made with ❤️ using Streamlit, VADER, and Hugging Face Transformers