# Movie-Recommendation-System

The project is a content based recommendation system which uses Bag of Words to recommend movies. Dataset for this project is TMDB which is available on kaggle. 
The features for the project which are considered are Description of the movie, Cast of the movie, crew of the movie then we convert this text into vectors and finally 
used Cosine Similarity as a metric to find the distance's between the vectors and recommend the movies which are near to the vector of the given movie, along with the 
names of the movie it also recommends the poster of the movie by calling the API of TMDB.
