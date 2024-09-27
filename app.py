# from typing import List, Any

# import streamlit as st
# import pickle
# import pandas as pd
# movies_dict=pickle.load(open('movies_dict.pkl','rb'))
# similarity=pickle.load(open('similarity.pkl','rb'))
# movies=pd.DataFrame(movies_dict)
# def recommend(movie):
#     movie_index = movies[movies['original_title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommend_new_movie=[]
#     for j in movie_list:
#         recommended_new_movie.append(movies.iloc[j[0]].original_title)
#     return recommended_new_movie
#
# st.title('Movie Recommender System')
# selected_movie_name=st.selectbox(
#     'How would you like to be contacted?',
#     movies['original_title'].values
# )
#
# if st.button('Recommend'):
#     recommendations=recommend('selected_movie_name')
#     for i in recommendations:
#         st.write(i)
#
import streamlit as st
import pickle
import pandas as pd

# Load the data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_new_movie = []
    for j in movie_list:
        # movie_id = j[0]
        recommended_new_movie.append(movies.iloc[j[0]].original_title)
    return recommended_new_movie

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['original_title'].values
)

# Button to trigger recommendation
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
