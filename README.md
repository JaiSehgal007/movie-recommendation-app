# Movie Recommendation System using Streamlit

## Overview

This project implements a movie recommendation system using a collaborative filtering approach. The recommendation system is built using Python, pandas, scikit-learn, NLTK, Gensim, and Streamlit. The dataset used for this project contains information about movies, including their titles, overviews, genres, keywords, cast, and crew.

## Features

- **Data Preprocessing**: The initial step involves cleaning and preprocessing the movie dataset. This includes handling null values, removing duplicates, and converting certain columns into a more usable format.

- **Text Processing**: The text data, such as overviews and tags, is processed to remove spaces and lemmatize the words using NLTK. This ensures consistency in word representation.

- **Word Embeddings with Word2Vec**: Gensim's Word2Vec model is employed to convert the processed text data into word embeddings. This is done to capture semantic relationships between words and enhance the recommendation system's understanding of movie similarities.

- **Streamlit App**: The recommendation system is integrated into a Streamlit web application. Users can select a movie from a dropdown menu and receive personalized movie recommendations.

- **Asynchronous Poster Fetching**: The app asynchronously fetches movie posters using The Movie Database (TMDb) API, enhancing the user experience by displaying relevant visuals.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/JaiSehgal007/movie-recommendation-app.git
```

2. Install dependencies:

Run the jupyter notebook file in the virtual environment to install all dependencies

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the provided URL in your web browser to access the Movie Recommender System.

## Files
data: Contains the dataset files (tmdb_5000_movies.csv and tmdb_5000_credits.csv).
app.py: The main Streamlit application file.
movie_recommendation.py: Python script containing the movie recommendation functions.
requirements.txt: List of Python dependencies.

## Additional Notes

Ensure you have a valid API key for TMDb. Set the `MOVIE_DB_API_KEY` environment variable with your key.
The project uses asynchronous programming for efficient poster fetching. It requires Python 3.7 or later.
Feel free to explore and enhance the project as needed. Happy movie recommending!




