# Airbnb Project Report #2

## Introduction

On the second stage of the project, I deep dived into regression and possible ways to maximize the utility of regressions through regularization. However, to achieve the best possible result I had to master the data preprocessing step to format the raw data and make it suitable for future use. After I perform all the necessary steps of dropping the insignificant data and formatting the existing one, linear models were applied to it, namely, Lasso & Ridge Regression (also known as $L_1$ and $L_2$ Regularization) as well as the combination of these two with polynomial regression. 

## Data Preprocessing /  A new approach

Even though most of the data preprocessing was explained in the previous report, during my research I stumbled upon an article that presented `Feature_Selector` - a Python library made to help during the data preprocessing stage and make the process smooth and easy. The description of the package can be found on [its GitHub page](https://github.com/Jie-Yuan/FeatureSelector). 

First, since the package does not come by default with the Python distribution it is necessary to install it using `pip install feature_selector`

Second, after creating a *FearureSelector* object we gain access to 5 methods by which missing data can be identified and handled:

1. Missing Values
2. Single Unique Values
3. Collinear Features
4. Zero Importance Features
5. Low Importance Features

By using the first method, Missing Values, we can create a histogram of the missing data. The parameters of the identify_missing method allow us to choose a threshold above which we want to find the missing data. For my purposes I use a threshold of 0 (meaning I want any proportion of missing values to be included. The data used for this plot is the raw data about Airbnb listings in Chicago accessible [here](http://insideairbnb.com/get-the-data.html). 

![missing_proportion.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e7a4ac5e-4379-466e-b967-65d9cc398ade/missing_proportion.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182226Z&X-Amz-Expires=86400&X-Amz-Signature=d4a465ad70be2c166c7caf618ed914142b5c92c5b879874fb6f5031595d3822d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22missing_proportion.png%22)

As we can see our raw data contains quite a few missing values. The bars on the left represent the columns (more than 30 in total) where the proportion of missing data is in range from 0 to 0.3 (on the x-axis). The bar on the most right represents 3 columns where exactly or more than 90% is missing. In case we want to break this plot down we can access the information regarding the proportions of missing values by calling the missing_stats method of our *FeatureSelector* (fs) object. 

[Untitled](https://www.notion.so/8888745abd7a403781c5ea7a9d280a60)

The single unique value method is not going to be explained in this report but it is very useful for columns with unevenly distributed data where one value dominates a large proportion of all data within the column. The next method is widely used and essential for a good machine learning model. For a good linear model to perform well it is essential to drop highly correlated feature and thus avoid multicollinearity. The reason for this is that highly correlated features are linearly dependent and hence have a similar effect on the target variable. First to understand the idea behind multicollinearity let us explore the correlations between all the variables in our dataset (excluding our target variable - *price*) by calling `fs.plot_collinear(plot_all=True)`.

![correaltions.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6f024537-3d27-43f3-8e6d-f8a1b1210cfa/correaltions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182431Z&X-Amz-Expires=86400&X-Amz-Signature=09091a9875d81e139e4ea1c238c15bb32a79e24c9efd68e8d6e8e86cf559f345&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22correaltions.png%22)

As we can see the large number of features does make it hard for us to manually identify features with high correlation. Luckily, the FeatureSelector object has `identify_collinear`

method that identifies features with correlation above the specified threshold. In my case, the threshold is going to be 0.8. Let us take a look at a reduced correlation matrix only containing features with correlation above the threshold. 

![correlations_above_.8.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4e50c168-2278-4564-8dad-0d49db2ab4c9/correlations_above_.8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182452Z&X-Amz-Expires=86400&X-Amz-Signature=9ee40c593ae29a36ad8c4eead1d13949a2a96e37bfb101f96e805784cd5cc11f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22correlations_above_.8.png%22)

If we want to access the full list of features that were identified to be highly correlated and need to be dropped we need to call `fs.ops['collinear']` . 

The other two methods of identifying insignificant data are both built upon the [LightGBM library](https://lightgbm.readthedocs.io/en/latest/Quick-Start.html) with which I am yet unfamiliar and therefore I am not going to rely much on these methods however I will still demonstrate their use. Zero importance features method requires us to specify the machine learning algorithm that we are going to implement and what metric is going to measure model's performance. In our case the task (the algorithm) is `regression` and the evaluation metric is `l2` or the mean squared error (the squared residual). Then if we want to see the bar plot of feature importances we can call `fs.plot_feature_importances` and get a similar looking plot. 

![feature_importance_barplot.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9b468810-65f9-4e50-bb25-d0252810dcb7/feature_importance_barplot.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182620Z&X-Amz-Expires=86400&X-Amz-Signature=0b0487ac440a09c8efa7b1b483ed660d90c147dd7038c8f6d70f1593e8163cef&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22feature_importance_barplot.png%22)

Moreover, we can specify and importance threshold within the `plot_feature_importances` function and see how many features our model requires to reach a certain level of cumulative importance. For my model I specified a threshold of 99%. 

![cum_importance.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3bdd74da-a2a0-4e42-a1ab-745f827270e3/cum_importance.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182640Z&X-Amz-Expires=86400&X-Amz-Signature=b94995ed88645046a1257669b5a9ee93237492581fb1289f80ee1b5dbb28793d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22cum_importance.png%22)

From the graph we can see that we need 36 out of our 40 features to reach a cumulative importance of 99%. If you are confused about the cumulative importance think of the 36 variables containing 99% of total information about the dataset, meaning that the other 4 features do not carry that much of importance. And, finally, the last method is the logical continuation of the previous one. It identifies the features that do not contribute to the cumulative importance past the threshold. On the plot above we can see that there are 4 variables to the right of the blue-dashed line, the following code is going to identify these variables: `identify_low_importance(cumulative_importance = 0.99).`

# Model Development

## Multiple Linear Regression

After preparing the dataset, I implemented a Linear Regression model accessible through the Sklearn library in python. Before we feed our data to the model we need to scale it (the process of scaling was explained in the Report #1). A generalized linear regression model has the following equation: $fθ(x)=θ_0+θ_1x_1+…+θ_px_p$, where $θ_p$ (theta) represents the coefficient assigned to the variable p and $x_p$ represents the variable itself. The goal of our model implemented using the Sklearn library is to minimize the cost function, i.e. find coefficients for each variable that result in the least possible sum of squares (distance between the predicted point and the original point). The cost function has the following form.

![regression.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/eac95e4c-aa58-4888-ad73-200cae434663/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182700Z&X-Amz-Expires=86400&X-Amz-Signature=404b63770ae5b2e02e812bd37fc57166e051898abb05a3887c826c44d9734eb5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

Our goal is to minimize the residuals of our data (minimize the sum of squares) and maximize the proportion of data explained by our model - $R^2$. R-squared ($R^2$) is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. For our first linear model the R-squared is equal to **0.3693**. Let's take a look at how residuals are positioned in comparison to the original data. On the plot, the points that were correctly predicted are positioned at the blue line. 

![predvsreal.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f5a07418-4f03-4f3d-996f-f415c452098a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T182943Z&X-Amz-Expires=86400&X-Amz-Signature=7c1ca0e3c01724ef9092c8bbf93ff2639730b1ae1283fc827ae910d35bc516aa&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

As we can see from the plot our model is far from ideal. Let us now modify our initial linear model by adding a new regularization term. 

## $L_1$ Regularization - Lasso Regression

Lasso Regression is a type of linear regression regularization, a method of penalizing large weights in our cost function to lower model variance. What it does is it adds a regularization (bias) term. Notice the equation below and compare it to the original cost function. Note that the new parameter  $λ$ is predefined and is used to finetune the model. Since the theta in the very end is put in absolute value it is possible for this model to assign 0 weights to certain variables. Therefore, Lasso can serve as a feature selection algorithm at the same time. To see the feature importance we can refer to the LASSO Path plot. There is much more to this plot other than feature selection, however for my current purposes it is going to serve as a complimentary visualization for the Lasso regression. Feature importances correspond to the order from left to right, the leftmost one being the most important (on the plot below it is the accommodates feature) and the rightmost one being the least important (maximum_nights). 

![lasso.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/38069a5c-2068-492a-8f03-e0e697862307/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183013Z&X-Amz-Expires=86400&X-Amz-Signature=088d0a1066a5c0e5a927670194a4f54bd2af96a77675c27a98d57699200928b0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![lasso_path.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/045665e7-a9c5-415f-be4d-63762f1eb85e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183034Z&X-Amz-Expires=86400&X-Amz-Signature=c881cf855d4e20f3ef188e0f0f345418bca3aae2b51fde6aaf787d3f9be8bfb3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

However, seemingly, because of the nature of our data, the Lasso regression did not significantly improve the $R^2$ and gave us a result of **0.3705.**

## $L_2$  Regularization - Ridge Regression

Ridge regression is almost identical to Lasso besides the coefficient $θ_p$ is squared (in Lasso the absolute value is taken). The formula for Ridge is of the following form: 

![ridge.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/76df80ba-6246-490c-8b2c-dcf43b381849/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183107Z&X-Amz-Expires=86400&X-Amz-Signature=41ff973b633b63c0889a4e3a958efab429c342962a87da18b6ba625b38f5b8da&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

The resulting $R^2$  is slightly higher relative to the Lasso's one but still is far from best: **0.3715.** 

## Polynomial Regression

At this stage it seems like we have achieved the maximum possible results given our dataset without altering the data. Now what we can do is to transform our model to a polynomial one. To understand the difference between the two take a loot at the pictures below. 

![poly.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8ea05851-5223-47af-867d-01d815c31133/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183125Z&X-Amz-Expires=86400&X-Amz-Signature=4451b9df073e8ec76352c892f4fac765f8f5c075f5405fed2a2a06cb4dff13a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![simplevsmultiple.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ad4774b3-cea5-424d-bb34-b1ede7777325/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183142Z&X-Amz-Expires=86400&X-Amz-Signature=bd675b097c163c11bbca1f7358a5fcfe4158426aa7e8b368cac10fceaa7000e7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

As we can see thanks to this transformation of our data, the model can predict the results better because the best-fit line is not straight anymore and hence can account for anomalies in our data. To understand the application of this model on our data let us apply the Polynomial Features method available from Sklearn and see the resulting variables. Note: for mathematical purposes instead of having names our variables are indexed from $x_0$  to $x_i$. 

> '1', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x0^2', 'x0 x1', 'x0 x2', 'x0 x3', 'x0 x4', 'x0 x5', 'x0 x6', 'x0 x7', 'x0 x8', 'x0 x9', ......... , 'x5^2', 'x5 x6', 'x5 x7', 'x5 x8', 'x5 x9', 'x6^2', 'x6 x7', 'x6 x8', 'x6 x9', 'x7^2', 'x7 x8', 'x7 x9', 'x8^2', 'x8 x9', 'x9^2'

Initially, our dataset contained only 10 features when now it contains 66 features (that is 56 more!). These variables are automatically generated and hence their relevance can differ. What we can do to undermine the new insignificant variables is to apply Lasso Regression to achieve a better result. The resulting $R^2$ is **0.432** which compared to other improvements is the biggest so far (the best result before was 0.3705). To visually trace the difference between the multiple linear regression model and this model take a look at how the predicted price values correspond to their originals. 

![Airbnb%20Project%20Report%20#2%20f520fa8508554f1fb8985e1e2e998ec2/Untitled%207.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/76bf266e-8adc-4f0b-8da8-5db15d121475/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183208Z&X-Amz-Expires=86400&X-Amz-Signature=6d13fed7175135bd8e3b558643115621c8cc97ea8b0fd294dbc5130556d6d1b3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![Airbnb%20Project%20Report%20#2%20f520fa8508554f1fb8985e1e2e998ec2/Untitled%208.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3c65074f-8b52-47e5-ab57-2cce4a97f96e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T183217Z&X-Amz-Expires=86400&X-Amz-Signature=73184cd3e62fc10c1c0c749a6138823bd8e3af1c31dbca228634ee3dc7fb68e4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
