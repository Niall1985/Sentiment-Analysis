# Sentiment Analysis using spaCy and VADER

This Python script analyzes the sentiment of text using spaCy for tokenization and VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis. It calculates sentiment scores and categorizes them as positive, negative, or neutral based on a threshold.

## Dependencies

- `spacy`: Python library for natural language processing.
- `vaderSentiment`: Python library for sentiment analysis.

### Install the required dependencies using pip:

```bash
pip install spacy vaderSentiment
```

### Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

## Usage

### 1. Clone the repository:
 ```bash 
git clone https://github.com/Niall1985/Sentiment-Analysis.git
cd your_repository-folder
code .
```

### 2. Run the script:
```bash
python Sentiment_analyzer.py
```

### 3. Follow the prompt and enter the review to be analyzed:
```bash
Enter the review to be analyzed here: This is a great product! I love it.
```

### The script will output sentiment scores and categorize the sentiment based on the compound score:
```bash 
Sentiment Score: {'neg': 0.0, 'neu': 0.435, 'pos': 0.565, 'compound': 0.6249}
Positive sentiment 😁
```

## Additional notes
### 1. Adjust the threshold (0.3 and -0.3) in the script to modify how sentiment is categorized as positive, negative, or neutral.
### 2. Ensure proper input format for accurate sentiment analysis results.

## License
### This project is licensed under the MIT License - see the LICENSE file for details.