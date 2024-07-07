import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

load_english_model = spacy.load('en_core_web_sm') #loads the spacy english model

def analyze_sentiment(review_to_be_analyzed):
    doc = load_english_model(review_to_be_analyzed)
    # print(doc)

    analyzer = SentimentIntensityAnalyzer() #initializes the VADER sentiment analyzer

    # Calculate sentiment scores
    sentiment_score = analyzer.polarity_scores(review_to_be_analyzed)

    return sentiment_score

review_to_be_analyzed = input("Enter the review to be analyzed here:")
sentiment_score = analyze_sentiment(review_to_be_analyzed)
print(f"Sentiment Score: {sentiment_score}")

#compound score calculation 
if sentiment_score['compound'] >= 0.3:
    print("Positive sentiment 😁")
elif sentiment_score['compound'] <= -0.3:
    print("Negative sentiment 😡")
else:
    print("Neutral sentiment 😐")
