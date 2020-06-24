# Airbnb Price Prediciton Project 

## Data Set
The dataset used fror this project contains the information about current Airbnb listing in the city of Chicago. The dataset was downloaded from http://insideairbnb.com/get-the-data.html. 
Inside Airbnb is an independent, non-commercial set of tools and data that allows its users to explore how Airbnb is really being used in cities around the world. Datasets found on InsideAirbnb contain many features such as the number of beds, number of guests allowed, description, number of reviews, location, and many more.

## Idea
What to predict:
Price of a given apartment/house based on the numerous present factors in the dataset as well as on the proximity of venues and places Price depending on the reviews 

Algorithms used: 
Linear, Lasso, Ridge, and Polynomial Regressions. 
Clustering with PCA 

## To-do list

* Step 1: Perform the necessary data cleaning and formating on the Chicago Airbnb dataset for future convenience. 
* Step 2: Develop a price prediction model using regression.
* Step 3: By using the Foursquare API (https://developer.foursquare.com/) add to the existing data set the information about the proximate places and venues (like pubs, clubs, theaters, museums, metro, etc.).
* Step 4: Using the information from step 3, identify what category of places or venues impacts the price the most. 
*Step 5: Make a number of visualizations to get a better understanding of the data. (Primarily geo-visualizations)
* Step 6: Develop a model based on the one developed on step 2 that predicts the price of a given house/apartment taking into account its location. 
* Step 7: Improve the model from step 6 with the help of the XGBoost Algorithm and perform some final tweaking of it. 
* Step 8: (Optional) Retrieve the data about big events in Chicago and confront it with the historical price of Airbnbs. 
* Step 9: (Optional) Develop a model that predicts the price of a listing given an event with a certain number of visitors 

## Resources 
1) https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN - Complete Machine Learning Course by Andrew NG  
2) https://campus.datacamp.com/courses/pandas-foundations/ - Pandas Foundations Course on DataCamp
3) https://learn.datacamp.com/courses/unsupervised-learning-in-python - Unsupervised Learning Course on DataCamp 
4) https://learn.datacamp.com/courses/supervised-learning-with-scikit-learn - Supervised Learning Cousr on DataCamp
5) https://www.textbook.ds100.org/intro.htmlPrinciples and Techniques of Data Science By Sam Lau, Joey Gonzalez, and Deb Nolan 
6) https://github.com/Jie-Yuan/FeatureSelector/blob/master/Feature%20Selector%20Usage.ipynb - Feature_Selector package 
7) https://towardsdatascience.com/airbnb-price-prediction-using-linear-regression-scikit-learn-and-statsmodels-6e1fc2bd51a6 - Simmilar Price Prediciton model for Airbnb data 
8) https://towardsdatascience.com/ridge-and-lasso-regression-a-complete-guide-with-python-scikit-learn-e20e34bcbf0b - Explanation of the theory behind Lasso and Ridge Regressions
9) https://www.youtube.com/watch?v=Q81RR3yKn30 - Ridge Regression 
10) https://www.youtube.com/watch?v=NGf0voTMlcs - Lasso Regression 
11) https://www.youtube.com/watch?v=1dKRdX9bfIo&t=219s - Elastic Net Regression  
12) https://www.youtube.com/watch?v=0GzMcUy7ZI0 - Theory behind PCA 
