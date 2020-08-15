# general
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import time

# modelling
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn.linear_model import LinearRegression,lars_path,LassoCV,RidgeCV, ElasticNet
from sklearn import linear_model
from sklearn import metrics
import xgboost as xgb
from xgboost import plot_importance
from sklearn.metrics import explained_variance_score, mean_squared_error, r2_score, max_error, mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV



def choose_csv():
    '''
    Returns the dataset you chose. 

    '''
    file_name = 'data\listings_cleaned_with_counts_final.csv'
    #file_name = 'data/' + input('Enter the name of your CSV file (Leave empty to call file explorer): ') 
    if not file_name:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        file_name = askopenfilename()
    print('CSV File Name: {}'.format(file_name))
    time.sleep(1)
    data_counts = pd.read_csv(file_name, index_col=['id'])
    # if 'id' in data:
    #     data.set_index('id')
    data_all = pd.read_csv('data/listings.csv',index_col=['id'])
    data_all = data_all.loc[data.index]
    data_raw = pd.read_csv('data/listings_cleaned.csv',index_col=['id'])
    return data_counts, data_all, data_raw

def drop():
    data, data_all, data_raw = choose_csv()
    if input('Do you want to drop columns? (y/n)') == 'y':
        print(list(data))
        to_drop = []
        to_drop.append(input('Enter Column Name: '))
        while input('Do you want to add more? (y/n)  ') == 'y':
            to_drop.append(input('Enter Column Name: '))
    if input('Do you want to include categorical data? (y/n) : ') == 'y':
        cols = ['neighbourhood_cleansed','property_type','room_type','bed_type','cancellation_policy']
        cat_cols = data_all[cols]
        data_for_modeling = pd.concat([data, cat_cols], axis=1)
        data_for_modeling = pd.get_dummies(data_for_modeling)
        data_for_modeling.columns = data_for_modeling.columns.str.replace(' ','_')
    else: 
        data_for_modeling = data
    missing = input('How do you want to handle the missing data? (drop/impute/0s) : ')
    if missing == 'drop':
        data_for_modeling = data_for_modeling.dropna(inplace = True)
    elif missing == '0s':
        data_for_modeling = data_for_modeling.fillna(0)
    else:
        from sklearn.experimental import enable_iterative_imputer
        from sklearn.impute import IterativeImputer
        imp = IterativeImputer(max_iter=5, random_state=0)
        data_for_modeling = imp.fit_transform(data_for_modeling)
    return data_for_modeling, data, data_raw


def linreg(X_train, X_test, y_train, y_test):
    lin_reg = LinearRegression()  
    lin_reg.fit(X_train, y_train)
    y_train_pred = lin_reg.predict(X_train)
    y_test_pred = lin_reg.predict(X_test)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("Linear Regression")
    print("\nTraining r2:", train_score) 
    print("Validation r2:", test_score)

def lasso(X_train, X_test, y_train, y_test):
    alphas = 10**np.linspace(-2,2,200)
    lasso = LassoCV(alphas=alphas,cv=10,tol=0.1).fit(X_train, y_train)
    y_train_pred = lasso.predict(X_train)
    y_test_pred = lasso.predict(X_test)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("Lasso Regression")
    print("\nTraining r2:", train_score)
    print("Validation r2:", test_score)

def ridge(X_train, X_test, y_train, y_test):
    alphas = np.linspace(0,2,100)
    ridge = RidgeCV(normalize=False,alphas=alphas,cv=10).fit(X_train, y_train) 
    y_train_pred = ridge.predict(X_train)
    y_test_pred = ridge.predict(X_test)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("Ridge Regression")
    print("\nTraining r2:", train_score)
    print("Validation r2:", test_score)

def poly_lasso():
    poly = PolynomialFeatures(degree=2).fit(X_train)
    X_train_poly = poly.transform(X_train) 
    X_test_poly = poly.transform(X_test)
    alphas = 10**np.linspace(-2,2,1000)
    lasso = LassoCV(alphas=alphas,cv=10,tol=0.1).fit(X_train_poly, y_train.ravel()) 
    y_train_pred = lasso.predict(X_train_poly)
    y_test_pred = lasso.predict(X_test_poly)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("Lasso Regression with Polynomial Features")
    print("\nTraining r2:", train_score)
    print("Validation r2:", test_score)

def poly_ridge():
    poly = PolynomialFeatures(degree=2).fit(X_train)
    X_train_poly = poly.transform(X_train) 
    X_test_poly = poly.transform(X_test)
    alphas = 10**np.linspace(-2,2,1000)
    ridge = RidgeCV(normalize=False,alphas=alphas,cv=10).fit(X_train_poly, y_train.ravel()) 
    y_train_pred = ridge.predict(X_train_poly)
    y_test_pred = ridge.predict(X_test_poly)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("Ridge Regression with Polynomial Features")
    print("\nTraining r2:", train_score)
    print("Validation r2:", test_score)


def boost(X_train, X_test, y_train, y_test):
    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.4, learning_rate = 0.15, max_depth = 4, booster='gbtree')
    xg_reg.fit(X_train,y_train)
    y_train_pred = xg_reg.predict(X_train)
    y_test_pred = xg_reg.predict(X_test)
    train_score = round(r2_score(y_train, y_train_pred),4)
    test_score = round(r2_score(y_test, y_test_pred),4)
    print("XGBoost")
    print("\nTraining r2:", train_score)
    print("Validation r2:", test_score)
    
def regressions():
    data_for_modeling, data, data_raw = drop()
    X = data_for_modeling.drop('price', axis=1)
    y = data_for_modeling.price
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
    

if __name__ == "__main__":
    start = time.time()
    #dataset = choose_csv()
    new = drop()
    #data_amenities = pois_amenities(dataset)
    #new_data = pois_subway(dataset)
    end = time.time()
    #save_csv(new_data)
    print('Run time: {:.2f} minutes'.format((end - start)/60))