# Airbnb Price Prediciton Project

This project's aim is to build a price prediction model based on Chicago Airbnb Listings dataset available from [InsideAirbnb](http://insideairbnb.com/get-the-data.html). The dataset is further extended by creating new variables based on geospatial analysis.

### Table of Contents

1. [Foreword](#foreword) 
2. [Installation](#installation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Resources](#resources)

## Foreword <a name="foreword"></a>

This project is a part of James Rocco Research Scholarship provided by Lake Forest College and was carried out under the supervision of Prof. Arthur Bousquet. The main idea is based on an article by Graciela Carrillo posted on [Towards Data Science](https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-location-data-5c1e033d0a5a). 

## Installation <a name="installation"></a>

Using Anaconda create a new environment from environment.yml. 

```python
conda env create --file environment.yml
```

## File Descriptions (Follow in order) <a name="files"></a>

To conveniently read all the notebooks follow this [link](https://nbviewer.jupyter.org/). 

1. [EDA.ipynb (Exploratory Data Analysis)](https://github.com/amac-lfc/airbnb/blob/master/EDA.ipynb) - A brief overview and analysis of raw data
2. [kepler_map.ipynb](https://github.com/amac-lfc/airbnb/blob/master/kepler_map.ipynb) - Visualization of the whole dataset using [Kepler.gl](http://kepler.gl) 
3. [data_preprocessing.ipynb](https://github.com/amac-lfc/airbnb/blob/master/data_preprocessing.ipynb) - Preprocessing the data for future uses (outlier detection, feature selection, handling missing data, etc.) 
4. [regressions.ipynb](https://github.com/amac-lfc/airbnb/blob/master/regressions.ipynb) - Development of initial price prediction models
5. [geo_loc.py](https://github.com/amac-lfc/airbnb/blob/master/geo_loc.py) - A python script for geospatial analysis: creates 5 new variables using such libraries as [OSMnx](https://github.com/gboeing/osmnx) and [OpenRouteSerivce](https://github.com/GIScience/openrouteservice-py):
    - Restaurants - Number of restaurants in a 1000 meters radius
    - Cafes - Number of cafes in the radius
    - Bars - Number of bard in the radius
    - CTA - Number of CTA (Chicago Subway) stations in the radius
    - time_to_cta_minutes - Time in minutes to the nearest CTA station (can be out of the radius)
6. [cta_mapping.ipynb](https://github.com/amac-lfc/airbnb/blob/master/cta_mapping.ipynb) - Visualization of geo_loc.py using [Folium](https://python-visualization.github.io/folium/index.html) maps (Map of routes to CTAs in the radius and shortest path detection)

## Results <a name="results"></a>


_ | Linear Regression | Lasso Regression | Ridge Regression | Lasso Regression with Polynomial Features| Ridge Regression with Polynomial Features | XGBoost | 
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
<b> No new variables: </b> <br/>Train R<sup>2</sup>  | 0.3646 | 0.3646 | 0.3646 | 0.4061 | 0.422 | 0.7112
Test R<sup>2</sup> | 0.4102 | 0.4104 | 0.4102 | 0.3903 | 0.4043 | 0.5816
<b> With new variables: </b> Train R<sup>2</sup> | 0.457 | 0.4552 | 0.4558 | 0.487 | 0.494 | 0.7173
Test R<sup>2</sup> | 0.4169 | 0.4163 | 0.4163 | 0.435 | 0.507 | 0.5417 



## Resources <a name="resources"></a>

1. [https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN) - Complete Machine Learning Course by Andrew NG
2. [https://campus.datacamp.com/courses/pandas-foundations/](https://campus.datacamp.com/courses/pandas-foundations/) - Pandas Foundations Course on DataCamp
3. [https://learn.datacamp.com/courses/unsupervised-learning-in-python](https://learn.datacamp.com/courses/unsupervised-learning-in-python) - Unsupervised Learning Course on DataCamp
4. [https://learn.datacamp.com/courses/supervised-learning-with-scikit-learn](https://learn.datacamp.com/courses/supervised-learning-with-scikit-learn) - Supervised Learning Cousr on DataCamp
5. [https://www.textbook.ds100.org/intro.htmlPrinciples](https://www.textbook.ds100.org/intro.htmlPrinciples) and Techniques of Data Science By Sam Lau, Joey Gonzalez, and Deb Nolan
6. [https://github.com/Jie-Yuan/FeatureSelector/blob/master/Feature%20Selector%20Usage.ipynb](https://github.com/Jie-Yuan/FeatureSelector/blob/master/Feature%20Selector%20Usage.ipynb) - Feature_Selector packagew
7. [https://towardsdatascience.com/airbnb-price-prediction-using-linear-regression-scikit-learn-and-statsmodels-6e1fc2bd51a6](https://towardsdatascience.com/airbnb-price-prediction-using-linear-regression-scikit-learn-and-statsmodels-6e1fc2bd51a6) - Simmilar Price Prediciton model for Airbnb data
8. [https://towardsdatascience.com/ridge-and-lasso-regression-a-complete-guide-with-python-scikit-learn-e20e34bcbf0b](https://towardsdatascience.com/ridge-and-lasso-regression-a-complete-guide-with-python-scikit-learn-e20e34bcbf0b) - Explanation of the theory behind Lasso and Ridge Regressions
9. [https://www.youtube.com/watch?v=Q81RR3yKn30](https://www.youtube.com/watch?v=Q81RR3yKn30) - Ridge Regression
10. [https://www.youtube.com/watch?v=NGf0voTMlcs](https://www.youtube.com/watch?v=NGf0voTMlcs) - Lasso Regression
11. [https://www.youtube.com/watch?v=1dKRdX9bfIo&t=219s](https://www.youtube.com/watch?v=1dKRdX9bfIo&t=219s) - Elastic Net Regression
12. [https://www.youtube.com/watch?v=0GzMcUy7ZI0](https://www.youtube.com/watch?v=0GzMcUy7ZI0) - Theory behind PCA
