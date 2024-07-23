import pickle

# Load the sentiment model from "sa_model.pkl"
with open(r'../data/sa_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Define a function to use the model for sentiment analysis
def analyze_sentiment(text):
    # Use the polarity_scores method of SentimentIntensityAnalyzer
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
