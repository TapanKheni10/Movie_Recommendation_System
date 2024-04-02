import streamlit as st
import pickle

st.set_page_config(
    page_title="Recommand Movies",
)

movies_list = pickle.load(open("artifacts/movies.pkl", "rb"))
movies = movies_list["title"].values

similarity = pickle.load(open("artifacts/similarity_matrix.pkl", "rb"))

def recommand(movie):
    movie_inx = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_inx]
    similar_movies = sorted(enumerate(distances), reverse=True, key=lambda x : x[1])[1:5]
    
    recommanded_movies = []
    for x in similar_movies:
        movie_id = x[0]
        recommanded_movies.append(movies_list.iloc[x[0]].title)

    return recommanded_movies

st.title("Movie Recommendation System", help="this will suggest some movies based on your content that you liked")

selected_movie = st.selectbox(
    "**select a movie from the drop down menu to get the recommendation of movies**",
    movies, 
    index=None,
    placeholder="select a movie to get the recommendation",
    label_visibility='hidden'
)

if st.button("Recommend a Movie"):
    recommendation = recommand(selected_movie)
    for i in recommendation:
        st.write(i)