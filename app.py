# using virtual env so that only those lib get installed on server which we currently need in this project
import pickle
import os
from dotenv import load_dotenv
import streamlit as st
import aiohttp
import asyncio

load_dotenv()
movie_db_api_key = os.getenv("MOVIE_DB_API_KEY")

async def fetch_poster(movie_id, session, max_retries=1):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={movie_db_api_key}&language=en-US"
    for retry in range(max_retries):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                poster_path = data['poster_path']
                full_path = "https://image.tmdb.org/t/p/w500" + poster_path
                return full_path
        except aiohttp.ClientError as e:
            st.warning(f"Error fetching poster (attempt {retry + 1}/{max_retries}): {e}")

    st.error("Failed to fetch poster after multiple attempts.")
    return None

async def fetch_all_posters(movie_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_poster(movie_id, session) for movie_id in movie_ids]
        return await asyncio.gather(*tasks)

async def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []

    movie_ids = [movies.iloc[Movie[0]].movie_id for Movie in movies_list]
    poster_urls = await fetch_all_posters(movie_ids)

    for name, url in zip(movie_list, poster_urls):
        recommended_movie_names.append(name)
        recommended_movie_posters.append(url)

    return recommended_movie_names, recommended_movie_posters

# Rest of your Streamlit code...

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    # Run the asynchronous code
    with st.spinner("Fetching recommendations..."):
        # Create an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Run the coroutine and get the result
        recommended_movie_names, recommended_movie_posters = loop.run_until_complete(recommend(selected_movie))
        
        # Display the recommendations
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if recommended_movie_posters[0] is not None:
                st.text(recommended_movie_names[0])
                st.image(recommended_movie_posters[0])
        with col2:
            if recommended_movie_posters[1] is not None:
                st.text(recommended_movie_names[1])
                st.image(recommended_movie_posters[1])
    with col3:
        if recommended_movie_posters[2] is not None:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
    with col4:
        if recommended_movie_posters[3] is not None:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
    with col5:
        if recommended_movie_posters[4] is not None:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])




