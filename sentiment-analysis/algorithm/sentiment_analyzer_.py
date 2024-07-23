import json
import time
from typing import Tuple, Dict, Any

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon only once
nltk.download('vader_lexicon', quiet=True)


def SentimentAnalyzer(data: dict) -> tuple[SentimentIntensityAnalyzer, dict[Any, float | int]]:
    print("Sentiment Analyzer")
    time.sleep(2)
    print(data)

    sia = SentimentIntensityAnalyzer()

    movie_sentiment = {}
    for movie, reviews in data.items():
        if reviews:  # Check if there are any reviews
            scores = [sia.polarity_scores(review)['compound'] for review in reviews]
            movie_sentiment[movie] = sum(scores) / len(scores)
        else:
            movie_sentiment[movie] = 0  # Handle case with no reviews
    return sia, movie_sentiment
