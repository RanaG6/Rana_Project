import streamlit as st
import pickle
import requests
import os

tmdb_api_key = "d8584d9731f055b8a1fe2b9acda41316"
tmdb_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkODU4NGQ5NzMxZjA1NWI4YTFmZTJiOWFjZGE0MTMxNiIsIm5iZiI6MTczNzYwMTAyMy41Nzc5OTk4LCJzdWIiOiI2NzkxYWZmZjIxMDQ4ZTlmNThmYTY3ZTciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.NdU5c0fBDqJyM7kvPWf62WSRf5zVz5A_S8wCTSDijKo"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()

    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

if not os.path.exists("movies_list.pkl") or not os.path.exists("similarity.pkl"):
    st.error("Required files 'movies_list.pkl' or 'similarity.pkl' not found.")
    st.stop()

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Choose a movie to get similar recommendations:", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
