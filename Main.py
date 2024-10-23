import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from spellchecker import SpellChecker
import json
import time


REVIEW_FILE = "extracted_reviews.txt"

def extract_reviews(website):
    # url = "https://www.trustpilot.com/review/" + website
    url = website
    with open(REVIEW_FILE, "w", encoding="utf-8", buffering=1) as file:
        page = 1
        while page != 10:
            urlNew = url + "?page=" + str(page)
            response = requests.get(urlNew)
            soup = BeautifulSoup(response.content, "html.parser")
            reviews = soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
            for review in reviews:
                try:
                    review_text = review.find('p', {'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}).text.strip()
                    file.write(review_text + "\n\n")
                except Exception:
                    review_text = None
            page += 1
            time.sleep(1)  
            
def append_pos_to_json(review, sentiment):
    with open("pos_json.json", "a", encoding="utf-8") as json_file:  
        json.dump({"review": review, "sentiment": sentiment}, json_file, indent=4)

def append_neg_to_json(review, sentiment):
    with open("neg_json.json", "a", encoding="utf-8") as json_file:
        json.dump({"review": review, "sentiment": sentiment}, json_file, indent=4)

def append_neu_to_json(review, sentiment):
    with open("neu_json.json", "a", encoding="utf-8") as json_file:
        json.dump({"review": review, "sentiment": sentiment}, json_file, indent=4)

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

def analyze_reviews():
    processed_reviews = set() 
    while True:
        with open(REVIEW_FILE, "r") as file:
            for line in file:
                review_to_be_analyzed = line.strip()
                if review_to_be_analyzed not in processed_reviews: 
                    preprocessed_review = preprocess_text(review_to_be_analyzed)
                    sentiment_score = analyze_sentiment(preprocessed_review)
                    
                    if sentiment_score['compound'] >= 0.31:
                        append_pos_to_json(preprocessed_review, "Positive")
                        print(f"review: {preprocessed_review}\nsentiment: {"Positive 😁"}")
                    elif sentiment_score['compound'] <= -0.01:
                        append_neg_to_json(preprocessed_review, "Negative")
                        print(f"review: {preprocessed_review}\nsentiment: {"Negative 😡"}")
                    else:
                        append_neu_to_json(preprocessed_review, "Neutral")
                        print(f"review: {preprocessed_review}\nsentiment: {"Neutral 😐"}")

                    processed_reviews.add(review_to_be_analyzed)  
        time.sleep(2) 

if __name__ == "__main__":
    # website = input("Enter the website to review: ")
    website = "https://www.trustpilot.com/review/www.communityphone.org"
    with ThreadPoolExecutor() as executor:
        executor.submit(extract_reviews, website)
        executor.submit(analyze_reviews)
