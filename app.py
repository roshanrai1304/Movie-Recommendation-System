
### To run the website
# streamlit run app.py

import streamlit as st
import pickle
import pandas as pd
import requests


def convert_list(arr) :
    l = []
    for i, item in enumerate(arr) :
        a = (i, item)
        l.append(a)

    return l

def fetch_poster(movie_id) :
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=51489d9f65fdd162141a59dbddf06c64&language=en-US'.format(movie_id))
    data = response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=51489d9f65fdd162141a59dbddf06c64&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(convert_list(distances), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Search Movies', movies['title'].values)

if st.button("Recommend") :
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
      # Add chart #1
      st.text(names[0])
      st.image(posters[0])
      
    with col2:
      # Add chart #1
      st.text(names[1])
      st.image(posters[1])
      
    with col3:
      # Add chart #1
      st.text(names[2])
      st.image(posters[2])
      
    with col4:
      # Add chart #1
      st.text(names[3])
      st.image(posters[3])
      
    with col5:
      # Add chart #1
      st.text(names[4])
      st.image(posters[4])

