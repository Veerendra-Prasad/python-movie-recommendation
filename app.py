import numpy as np
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained vectorizer and TF-IDF matrix
with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('model/tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

# Load metadata (movie titles and other features)
movies_df = pd.read_csv('dataset/movie_dataset.csv')  # Ensure this CSV has at least a 'title' column

# Recommendation logic

def recommend_from_liked(liked_titles, top_n=10):
    """
    Given a list of liked movie titles, return top_n recommended movie titles
    based on cosine similarity of TF-IDF features.
    """
    # Find indices for liked movies
    liked_indices = []
    for title in liked_titles:
        match = movies_df[movies_df['title'].str.lower() == title.lower()]
        if not match.empty:
            liked_indices.append(match.index[0])

    # If none of the liked titles are found, return empty list
    if not liked_indices:
        return []

    # Compute mean vector of liked movies
    # Convert sparse matrix slices to dense arrays
    liked_vectors = tfidf_matrix[liked_indices].toarray()
    mean_vector = np.mean(liked_vectors, axis=0).reshape(1, -1)

    # Compute cosine similarity between mean_vector and all movie vectors
    # Convert full tfidf_matrix to array for similarity
    similarities = cosine_similarity(mean_vector, tfidf_matrix.toarray()).flatten()

    # Rank movies by similarity, exclude already liked
    ranked_indices = np.argsort(similarities)[::-1]
    recommendations = []
    for idx in ranked_indices:
        if idx not in liked_indices:
            recommendations.append(movies_df.iloc[idx]['title'])
        if len(recommendations) >= top_n:
            break

    return recommendations

# API endpoints

@app.route('/')
def home():
    return jsonify({"message": "Movie Recommendation API is up!"})

@app.route('/recommend', methods=['POST'])
def recommend_route():
    data = request.get_json()
    # Extract list of liked movies from request payload
    liked_movies = data.get('liked_movies', [])

    if not isinstance(liked_movies, list) or not liked_movies:
        return jsonify({"error": "Please provide a non-empty list of liked_movies"}), 400

    # Get recommendations
    recs = recommend_from_liked(liked_movies, top_n=10)
    return jsonify({"recommendations": recs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
