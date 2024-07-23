import json


# Define thresholds for categories
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


# Load sentiment scores
with open(r"../data/sentiment_scores.json") as scores_file:
    sentiment_scores: dict = json.load(scores_file)

# Print the number of sentiment scores
print(f"Number of sentiment scores: {len(sentiment_scores)}")

# Categorize the sentiment scores
categorized_scores: dict = {}
for movie, score in sentiment_scores.items():
    categorized_scores[movie]: str = categorize_score(score)

# Print the categorized scores
for movie, category in categorized_scores.items():
    print(f"Movie: {movie}, Category: {category}")

# Save the categorized scores to a JSON file
with open(r"../data/categorized_sentiment_scores.json", 'w') as output_file:
    json.dump(categorized_scores, output_file, indent=4)

print("Categorized sentiment scores have been saved to categorized_sentiment_scores.json")
