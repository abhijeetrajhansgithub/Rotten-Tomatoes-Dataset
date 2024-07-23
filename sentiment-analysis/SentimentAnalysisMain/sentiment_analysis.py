import pickle

from algorithm.sentiment_analyzer_ import SentimentAnalyzer
import json

# Load the movie review data
with open(r'../data/movie_name_dict.json', 'r') as f:
    movie_name_dict = json.load(f)

print(movie_name_dict)

# Analyze sentiment
sa, movie_sentiment = SentimentAnalyzer(movie_name_dict)

# Save the movie data sentiment analysis model
with open(r'../data/sa_model.pkl', 'wb') as f:
    pickle.dump(sa, f)

# Print sentiment for each movie
for movie_name, sentiment in movie_sentiment.items():
    print(f"Movie: {movie_name}, Sentiment Score: {sentiment}")

# Save the sentiment for each movie
with open(r'../data/sentiment_scores.json', 'w') as f:
    json.dump(movie_sentiment, f)
