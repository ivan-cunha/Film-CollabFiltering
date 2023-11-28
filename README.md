# Movie Recommendation System using Collaborative Filtering
## Overview
This project aims to build a movie recommendation system using collaborative filtering. Collaborative filtering is a popular technique in recommendation systems that relies on user-item interactions to make predictions and recommendations. In this case, the system leverages user ratings of movies to suggest new movies to users based on the preferences of similar users.

## Introduction
Collaborative filtering is a method that makes automatic predictions (filtering) about the preferences of a user by collecting preferences from many users (collaborating). In the context of movie recommendation, it means suggesting movies to a user based on the preferences and ratings of similar users. There are two main types of collaborative filtering: user-based and item-based. There are 2 notebooks, each with one implementation. The more detailed notebook is the implementation with user-user. The implementations are not the most eficient or fastest. This was done with the intent to study the algorithm, not to be implemented in a real world situation.

## How it Works
### User-Based Collaborative Filtering
User-based collaborative filtering recommends items based on the preferences of users who are similar to the target user. If User A and User B have similar movie preferences and User A liked a movie that User B hasn't seen, the system may recommend that movie to User B.

### Item-Based Collaborative Filtering
Item-based collaborative filtering recommends items based on their similarity to items the user has already shown interest in. If a user liked Movie X, and Movie Y is similar to Movie X, the system may recommend Movie Y to the user.

## Dataset
The success of collaborative filtering relies heavily on the quality of the dataset. The dataset used in this project contains user ratings for a variety of movies. It includes information about users, movies, and the ratings given by users to different movies.

## Implementation
The collaborative filtering recommendation system is implemented using numpy and pandas. The code is structured into modules for data preprocessing, model training and testing.

## Dependencies
* pandas
* numpy

## Results
The results of both methods are in the table bellow, note that user-user was a bit better for this case, but only a little. The margins will help to make sure a estimated rating will be good enouth.
| Metric      | User-User | Item-Item |
| ----------- | --------- | --------- |
| Lower Bound | -0.934    | -0.974    |
| High Bound  | 0.840     | 0.823     |
| MSE         | 0.526     | 0.546     |
| MAE         | 0.557     | 0.563     |
| RMSE        | 0.725     | 0.739     |