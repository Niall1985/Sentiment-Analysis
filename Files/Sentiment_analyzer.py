import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from spellchecker import SpellChecker
import json

def append_pos_to_json(review, sentiment):
    with open("pos_json.json", "w", encoding="utf-8") as json_file:
        json_file.write('[\n')
        json.dump({"review":review, "sentiment":sentiment}, json_file, indent=4)

def append_neg_to_json(review, sentiment):
    with open("neg_json.json", "w", encoding="utf-8") as json_file:
        json_file.write('[\n')
        json.dump({"review":review, "sentiment":sentiment}, json_file, indent=4)

def append_neu_to_json(review, sentiment):
    with open("neu_json.json", "w", encoding="utf-8") as json_file:
        json_file.write('[\n')
        json.dump({"review":review, "sentiment":sentiment}, json_file, indent=4)

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

with open("extracted_reviews.txt", "r") as file:
    for line in file:
        review_to_be_analyzed = line.strip()
 
preprocessed_review = preprocess_text(review_to_be_analyzed)

print(f"Corrected Sentence: {preprocessed_review}")

sentiment_score = analyze_sentiment(preprocessed_review)
print(f"Sentiment Score: {sentiment_score}")

if sentiment_score['compound'] >= 0.31:
    print("Positive sentiment 😁")
    append_pos_to_json(preprocessed_review, "Positive")
    
elif sentiment_score['compound'] <= -0.01:
    print("Negative sentiment 😡")
    append_neg_to_json(preprocessed_review, "Negative")

else:
    print("Neutral sentiment 😐")
    append_neu_to_json(preprocessed_review, "Neutral")
