import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))

st.header("Movie Recommender System")
st.selectbox("Select mvoie from dropdown", movies)

if st.button("Show Recommend");
    pass
