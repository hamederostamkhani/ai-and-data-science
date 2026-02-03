import streamlit as st
from recommender import MovieRecommender

st.title("Movie Recommender System")

rec = MovieRecommender()

movie_name = st.selectbox("Select a movie name:", rec.movie_list)

if st.button("Recommend"):
    recommendations = rec.recommend(movie_name)
    st.subheader("Top 10 movies which are similar to '" + movie_name + "' :")
    st.write(recommendations)
