# Movie Review Sentiment Analysis

This project focuses on analyzing the sentiment of movie reviews using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library. The process involves data preprocessing, sentiment analysis, and categorization of sentiment scores.

## Table of Contents
- [Requirements](#requirements)
- [Data Preprocessing](#data-preprocessing)
- [Sentiment Analysis](#sentiment-analysis)
- [Categorizing Sentiment Scores](#categorizing-sentiment-scores)
- [Usage](#usage)
- [Examples](#examples)
- [Saving and Loading the Model](#saving-and-loading-the-model)

## Requirements

To run this project, you need the following libraries:
- `nltk`
- `json`
- `csv`
- `pickle`

You can install the required libraries using pip:
```
pip install nltk
```

## Data Preprocessing
The data preprocessing step involves reading movie reviews from a CSV file, converting necessary columns to appropriate data types, and organizing the data for sentiment analysis.

```
import csv

def data_preprocessing():
    with open(r'../data/rotten_tomatoes_movie_reviews.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            line['id'] = str(line['id'])

def filter_data():
    movie_name_set = set()
    movie_name_dict = {}

    with open(r'../data/rotten_tomatoes_movie_reviews.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            movie_name_set.add(line['id'])

    for movie in movie_name_set:
        movie_name_dict[movie] = []

    with open(r'../data/rotten_tomatoes_movie_reviews.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['id'] in movie_name_set:
                movie_name_dict[line['id']].append(line['reviewText'])

    with open(r'../data/movie_name_dict.json', 'w') as json_file:
        json.dump(movie_name_dict, json_file)

if __name__ == '__main__':
    data_preprocessing()
    filter_data()

```

## Sentiment Analysis
The sentiment analysis step uses the VADER sentiment analysis tool to analyze the sentiment of the reviews.

```
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def SentimentAnalyzer(data: dict) -> dict:
    sia = SentimentIntensityAnalyzer()
    movie_sentiment = {}
    for movie, reviews in data.items():
        if reviews:
            scores = [sia.polarity_scores(review)['compound'] for review in reviews]
            movie_sentiment[movie] = sum(scores) / len(scores)
        else:
            movie_sentiment[movie] = 0
    return movie_sentiment

# Load and analyze sentiment
with open(r"../data/movie_name_dict.json") as f:
    movie_name_dict = json.load(f)
    sentiment_scores = SentimentAnalyzer(movie_name_dict)

# Save the sentiment scores
with open(r"../data/sentiment_scores.json", 'w') as f:
    json.dump(sentiment_scores, f)
```

## Categorizing Sentiment Scores
After analyzing the sentiment, the sentiment scores are categorized into predefined categories.

```
import json

def categorize_score(score):
    if score <= -0.6:
        return "extremely bad"
    elif -0.6 < score <= -0.2:
        return "bad"
    elif -0.2 < score <= 0.0:
        return "mediocre"
    elif 0.0 < score <= 0.2:
        return "okay"
    elif 0.2 < score <= 0.4:
        return "good"
    elif 0.4 < score <= 0.6:
        return "very good"
    else:
        return "excellent"

with open(r"../data/sentiment_scores.json") as scores_file:
    sentiment_scores = json.load(scores_file)

categorized_scores = {}
for movie, score in sentiment_scores.items():
    categorized_scores[movie] = categorize_score(score)

with open(r"../data/categorized_sentiment_scores.json", 'w') as output_file:
    json.dump(categorized_scores, output_file, indent=4)
```

## Usage
To use the sentiment analysis model, load the model from the pickle file and analyze the sentiment of new reviews.

```
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the sentiment model from "sa_model.pkl"
with open(r'../data/sa_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to use the model for sentiment analysis
def analyze_sentiment(text):
    scores = model.polarity_scores(text)
    return scores['compound']

# Example usage of the model
example_reviews = [
    "I absolutely loved this movie! It was fantastic.",
    "The movie was okay, not the best I've seen.",
    "I didn't like the movie at all. It was terrible."
]

# Analyze sentiment for each example review
for review in example_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}\nSentiment Score: {sentiment}\n")
```


This `README.md` file provides a comprehensive guide on how to set up, use, and understand the project. It includes detailed explanations of each step, the code involved, and example outputs.

---

# Author
This project was developed by Abhijeet Rajhans.
