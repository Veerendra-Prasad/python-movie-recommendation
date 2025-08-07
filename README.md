# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built using **Flask** (for the backend API) and **Python (Scikit-learn)** for Machine Learning. It recommends top 10 movies based on the movies liked by the user using metadata such as genres, keywords, director, etc.

---

## 🚀 Features

- Accepts a list of movies liked by the user
- Uses a pre-trained vectorizer and similarity matrix for content-based filtering
- Returns top 10 similar movies
- Built as a REST API using Flask
- Ready to be integrated into full-stack web apps

---

## 📁 Project Structure

```
movie-recommendation/
│
├── Dockerfile              # dockerfile for image building
├── app.py                  # Main Flask app
├── model/
|   |
|   ├── predict.py          # contains the main code for the model
│   ├── model.pkl           # Content-based recommendation model (cosine similarity matrix)
│   └── vectorizer.pkl      # Fitted TF-IDF vectorizer
├── dataset/
│   └── movie_dataset.csv   # Source data used to train the model
├── requirements.txt        # Python dependencies
├── .gitignore              # Files/folders ignored by Git
└── README.md               # Project overview (you’re here!)
```

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Veerendra-Prasad/python-movie-recommendation.git
cd python-movie-recommendation
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

The app will run at `http://127.0.0.1:5000/`.

---

## 📡 API Usage

### Endpoint

```http
POST /recommend
```

### Request Body (JSON)

```json
{
  "liked_movies": ["Inception", "Interstellar", "The Dark Knight"]
}
```

### Response

```json
{
  "recommended_movies": [
    "Memento",
    "The Prestige",
    "Batman Begins",
    "..."
  ]
}
```

---

## 🤖 How It Works

- The dataset is preprocessed to create a combined "features" column using metadata like genres, keywords, director, etc.
- A TF-IDF vectorizer transforms the features into vectors.
- Cosine similarity is calculated between all movie vectors.
- When a user sends liked movies, their vectors are combined and compared against all other movies to return the most similar ones.

---

## 📦 Dependencies

- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 🧠 Future Improvements

- Add collaborative filtering model
- Support user authentication and user history
- Deploy using Docker and integrate into full-stack app

---

## 📜 License

This project is licensed under the MIT License.