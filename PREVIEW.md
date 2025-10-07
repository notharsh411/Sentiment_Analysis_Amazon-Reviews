# 📱 App Preview - Real-time Review Sentiment Classifier

## 🎨 Visual Layout

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  📊 Real-time Review Sentiment Classifier                                ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                                           ┃
┃  This application analyzes the sentiment of product reviews in           ┃
┃  real-time using two powerful techniques:                                ┃
┃  • VADER: A lexicon and rule-based sentiment analysis tool              ┃
┃  • RoBERTa: A transformer-based deep learning model from Hugging Face   ┃
┃                                                                           ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ 📋 SIDEBAR                     ┃  📝 MAIN CONTENT AREA                   ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                ┃                                          ┃
┃  ℹ️ About                      ┃  ┌────────────────────────────────────┐ ┃
┃                                ┃  │ Enter your review:                 │ ┃
┃  How it works:                 ┃  │                                    │ ┃
┃  1. Enter review text          ┃  │ [Text area for user input]         │ ┃
┃  2. Choose models              ┃  │                                    │ ┃
┃  3. Get instant scores         ┃  │                                    │ ┃
┃                                ┃  └────────────────────────────────────┘ ┃
┃  Models:                       ┃                                          ┃
┃  • VADER: Fast, interpretable  ┃  Select Analysis Model:                 ┃
┃  • RoBERTa: Advanced NLP       ┃  ☑ VADER        ☑ RoBERTa              ┃
┃                                ┃                                          ┃
┃  ─────────────────────         ┃  ┌────────────────────────────────────┐ ┃
┃                                ┃  │   🔍 Analyze Sentiment             │ ┃
┃  Example Reviews:              ┃  └────────────────────────────────────┘ ┃
┃  [Try Positive Example]        ┃                                          ┃
┃  [Try Negative Example]        ┃                                          ┃
┃  [Try Neutral Example]         ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ┃
┃  [Try Mixed Example]           ┃                                          ┃
┃                                ┃  📈 ANALYSIS RESULTS                    ┃
┃                                ┃                                          ┃
┃                                ┃  ┌─────────────────┬─────────────────┐ ┃
┃                                ┃  │ 🎯 VADER        │ 🤖 RoBERTa      │ ┃
┃                                ┃  │ Analysis        │ Analysis        │ ┃
┃                                ┃  ├─────────────────┼─────────────────┤ ┃
┃                                ┃  │ Overall:        │ Overall:        │ ┃
┃                                ┃  │ 😊 Positive     │ 😊 Positive     │ ┃
┃                                ┃  │                 │                 │ ┃
┃                                ┃  │ Detailed:       │ Detailed:       │ ┃
┃                                ┃  │ Positive: 0.756 │ Positive: 0.892 │ ┃
┃                                ┃  │ Neutral:  0.244 │ Neutral:  0.098 │ ┃
┃                                ┃  │ Negative: 0.000 │ Negative: 0.010 │ ┃
┃                                ┃  │ Compound: 0.891 │                 │ ┃
┃                                ┃  └─────────────────┴─────────────────┘ ┃
┃                                ┃                                          ┃
┃                                ┃  📊 Model Comparison                    ┃
┃                                ┃  ┌────────────────────────────────────┐ ┃
┃                                ┃  │     [Bar Chart Visualization]      │ ┃
┃                                ┃  │  ▓▓▓ VADER   ░░░ RoBERTa          │ ┃
┃                                ┃  │  Negative | Neutral | Positive     │ ┃
┃                                ┃  └────────────────────────────────────┘ ┃
┃                                ┃                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## 🎯 Key Features Demonstrated

### 1. **Input Section**
- Large text area for entering product reviews
- Character and word count displayed in real-time
- Quick stats panel on the right side

### 2. **Model Selection**
- Checkboxes to select VADER, RoBERTa, or both
- Flexible analysis options

### 3. **Example Reviews (Sidebar)**
Pre-loaded examples you can click:
- ✅ **Positive**: "This product is absolutely amazing! Best purchase I've ever made. Highly recommend!"
- ❌ **Negative**: "Terrible quality. Broke within a week. Complete waste of money."
- ➖ **Neutral**: "The product arrived on time. It works as described in the specifications."
- 🔄 **Mixed**: "The product quality is good but the customer service was disappointing."

### 4. **Results Display**

#### VADER Analysis Results
```
┌─────────────────────────┐
│  Overall Sentiment:     │
│  😊 Positive            │
│                         │
│  Detailed Scores:       │
│  Positive:    0.756     │
│  Neutral:     0.244     │
│  Negative:    0.000     │
│  Compound:    0.891     │
└─────────────────────────┘
```

#### RoBERTa Analysis Results
```
┌─────────────────────────┐
│  Overall Sentiment:     │
│  😊 Positive            │
│                         │
│  Detailed Scores:       │
│  Positive:    0.892     │
│  Neutral:     0.098     │
│  Negative:    0.010     │
└─────────────────────────┘
```

### 5. **Interactive Visualization**
Side-by-side bar chart comparing:
- VADER scores (light blue bars)
- RoBERTa scores (salmon/pink bars)
- Three categories: Negative, Neutral, Positive

## 🎨 Color Scheme

- **Positive Sentiment**: Green background with 😊 emoji
- **Negative Sentiment**: Red background with 😞 emoji
- **Neutral Sentiment**: Yellow/orange background with 😐 emoji
- **Primary Color**: Red (#FF4B4B)
- **Charts**: Color-coded bars (#FF6B6B for negative, #FFE66D for neutral, #4ECDC4 for positive)

## 🔄 Example Workflow

1. **User enters**: "This coffee maker is fantastic! Makes perfect coffee every time. Love it!"
   
2. **VADER Analysis Shows**:
   - Overall: 😊 Positive
   - Compound: 0.8915
   - High positive score (0.587)
   
3. **RoBERTa Analysis Shows**:
   - Overall: 😊 Positive
   - Positive probability: 0.942
   - Very low negative probability

4. **Comparison Chart**: Shows both models agree strongly on positive sentiment

## 🚀 How to See This Live

Run the following command in your terminal:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` with all these features fully interactive!

## 💡 Interactive Elements

- ✅ Real-time text input with live stats
- ✅ Clickable example buttons that auto-fill text
- ✅ Model selection checkboxes
- ✅ Animated loading spinner during analysis
- ✅ Interactive Plotly charts (hover for details)
- ✅ Color-coded sentiment alerts
- ✅ Responsive layout that works on different screen sizes

---

**Ready to analyze your reviews? Just run the app and start typing!** 🚀