import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from spellchecker import SpellChecker


load_english_model = spacy.load('en_core_web_sm')

spell = SpellChecker()

def correct_spelling(word):
    return spell.candidates(word).pop() if spell.candidates(word) else word

def preprocess_text(text):
    words = text.split()
    corrected_words = [correct_spelling(word) for word in words]
    return ' '.join(corrected_words)

def analyze_sentiment(review_to_be_analyzed):
    doc = load_english_model(review_to_be_analyzed)
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(review_to_be_analyzed)
    return sentiment_score

review_to_be_analyzed = input("Enter the review to be analyzed here:")

preprocessed_review = preprocess_text(review_to_be_analyzed)

print(f"Corrected Sentence: {preprocessed_review}")

sentiment_score = analyze_sentiment(preprocessed_review)
print(f"Sentiment Score: {sentiment_score}")

if sentiment_score['compound'] >= 0.31:
    print("Positive sentiment 😁")
elif sentiment_score['compound'] <= -0.01:
    print("Negative sentiment 😡")
else:
    print("Neutral sentiment 😐")
