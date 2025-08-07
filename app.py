from flask import Flask, request, jsonify
from model.predict import recommend_from_liked
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)
frontend_url = os.getenv('FRONTEND_URL')
CORS(app, origins=[frontend_url])

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
