# Airbnb Project Report #1

by Samvel Gevorgyan 

## Purpose of this project

The primary goal of this project is to trace the relationship between various factors that characterize a given Airbnb listing and its price. Since most of the features (like number of beds, bathrooms, etc.) are not unique to a given listing, i.e. are not representative enough of the price variable, a big emphasis is going to be put on the location of the listing. From my and other people's experience with Airbnb it is a known fact that listing with the best location (primarily in the city or the business centers) have the highest prices. In this project I will be trying to define what is the best location. 

## Exploratory Data Analysis

Before I jump into the primary goal of the project, it is necessary to understand the data. Exploratory Data Analysis is a set of methods used by Data Scientists for these purposes. Moreover, while exploring the data, I can trace its inconsistencies (missing values, wrong data types, etc.). 

First of all, for the purposes of primary exploratory data analysis I am dropping the columns that mostly contain string objects (text) and hence are not very useful in exploring the data. 

However, the non-numeric variables are not the only problem, there are still numerous variables present in the dataset that are not very necessary and instead of helping us understand and read the data, they add extra complexity that can be avoided. 

Let's look into one of these variables called 'maximum_minimum_nights'. Due to the lack of documentation for the dataset I was unable to identify the purpose of this variable. Before thoughtlessly dropping this and other similar variables, let's take a look at how does this data fit in the overall model. For this, I will be using the KMeans clustering algorithm that (on the very basic levels) finds patterns in the data and groups it into specified number of clusters K. In order to choose the best number of clusters something called the 'elbow method' is used, it will be clear in a moment why it is called like this. For us to see the 'elbow' I will initialize a function that plots the inertias (or the distance to centroids, points that best describe a given cluster, identified by the KMeans) depending on the number of clusters. 

![intertias_linegraph_with_extra_variables.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/540cc530-1432-448b-a96e-fb8604e93127/intertias_linegraph_with_extra_variables.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T180159Z&X-Amz-Expires=86400&X-Amz-Signature=f8a1d13778cd76c893cc327c4bb98196edb575e54c84ea96439ba1f8bedf4455&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22intertias_linegraph_with_extra_variables.png%22)

Oh! Something went completely wrong in here. Let's figure out what is the matter. 

[Sample Statistics ](https://www.notion.so/640a2f79360749e5b539f990bcd46b0b)

As we can see from the selected variables above the standard deviations differ greatly meaning that it is impossible to compare them. For this very reason the graph above had that incorrect shape. 

What we can do about this is to scale our data. Scaling the data means to bring it into some standardized form. In this case I will be using StandardScaler function available from the Sklearn library. What it does, it sets the mean to 0 and the standard deviation to 1 for every individual variable. 

$$z = (x - \mu) / \sigma  $$

After applying the method on our data and calling the inertia ~ cluster graph again we can see an obvious improvement in our model.

![intertias_linegraph_with_extra_variables_scaled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0d345dfc-9a02-4274-988b-9b2b6c00dcf5/intertias_linegraph_with_extra_variables_scaled_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T180547Z&X-Amz-Expires=86400&X-Amz-Signature=3a6de0ce7c71a623fcad10e3c006a1decbc90a0900912ece8bdff581c55333cf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22intertias_linegraph_with_extra_variables_scaled_%281%29.png%22)

But where is the elbow? The problem now lies in those extra variables that do not bear any statistical significance to our model. Let's remove them, scale our data again and see the results. 

![Airbnb%20Project%20Report%20#1%208ac7054dc59446eab784798518d7ed72/inertias_linegraph_(1).png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ba48c27f-a9a0-42fd-8db9-19f5b4a48f28/inertias_linegraph_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T180612Z&X-Amz-Expires=86400&X-Amz-Signature=05ce7951c66559bdf3f845cbca126d8478e070c70a07c207a5338f66b8ff046b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22inertias_linegraph_%281%29.png%22)

This looks much better! As we can see the elbow lies between k equaling 2 and 4, meaning that the best suitable number of clusters is 3. Now when our data is ready for further exploration, let see the relationship between some of the variables and the price. 

![Accomodates___Price_Scatter.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b02ba041-683b-41f8-9398-d0d5ecf75ffd/Accomodates___Price_Scatter.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T180653Z&X-Amz-Expires=86400&X-Amz-Signature=433543043f8c9ba993d5a47f28b7444576db8f3df42754d5b02e8fecb768e407&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Accomodates___Price_Scatter.png%22)

On the scatterplot above the price is on the x-axis and the number a given listing can accommodate on the y-axis. From the graph we can see that there is no clear relationship between these two variable but what we can see is the presence of multiple outliers that might negatively impact our data. It is apparent that most of the data lies in the lower price range (below 2000). Moreover, in the future the goal is to be able to predict the best price for a property when listed on Airbnb and these 'special' cases are not the goal of the model, therefore let's focus on the 'normal' cases. We want to know what percentage of the data lies above the $2000, $1000, and $800 mark and if it is small enough we can drop these 'special' listings. Also, let's check for faulty listings with a price of 0 dollars. 

Output of the function checking these 4 statements:

> *Percentage of listings with price greater than $2000: 0.41079812206572774 %
Percentage of listings with price greater than $1000: 0.9624413145539906 %
Percentage of listings with price greater than $800: 1.9014084507042253 %
Number of listing with price equal to zero: 3*

As we can see roughly only 2% of all data lies above the $800 per night mark. If we drop this 2 percent it is not going to be a great loss and it will make it possible for us to focus on the 'normal' listings ($800 per night is luxurious enough). 

![baths___price_scatter.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/133ab4d3-106d-4fe6-9885-eaa2fe20fbc7/baths___price_scatter_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181342Z&X-Amz-Expires=86400&X-Amz-Signature=f339343c13afc624b3f156facf0dff395d5ab4449da5d781a3a9cebbe688c23a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22baths___price_scatter_%281%29.png%22)

The scatterplot above shows a similar relationship to the last one, but this time with the number of bathrooms on the y-axis. Also since we dropped the extra luxurious listings, the data seems to be better distributed but with an apparent left skew. This further can be seen when we plot a boxplot of the 'price' variable. 

![price_box.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2ece2fea-db37-4b8f-b48f-e2b37d67de3c/price_box.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181407Z&X-Amz-Expires=86400&X-Amz-Signature=e1b2e271dbb27dffb42fe54c4f08b68f613d50598eef0a807405f5bfc70933d5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22price_box.png%22)

Now, finally, let's apply the KMeans clustering on out data and see if there is any clear and apparent way to trace the origin of the clusters, i.e. what variable is the most representative of clusters. 

![number_of_reviews___price___colored.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a1ff7aa2-d543-4226-8681-3a7dd58b1891/number_of_reviews___price___colored_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181431Z&X-Amz-Expires=86400&X-Amz-Signature=0a500e3cf678decc7ebd7fc780d851a61fc55d768480798d831db8c64bc1db97&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22number_of_reviews___price___colored_%281%29.png%22)

![baths___price___colored_(1).png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/044cf3c4-3c45-49a9-85c3-922178555807/baths___price___colored_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181501Z&X-Amz-Expires=86400&X-Amz-Signature=3024bf67432aed0398eb968d1292e8694a93d10b61b5fd87347f470c74df82ec&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22baths___price___colored_%281%29.png%22)

![accomodates___price___colored_(1).png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/112d321c-ea90-49e0-b93b-ec884dd79b31/accomodates___price___colored_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181520Z&X-Amz-Expires=86400&X-Amz-Signature=7039c636c1527e5f542cf20f0da33139cb282b330606b13a53fceaf420c94a98&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22accomodates___price___colored_%281%29.png%22)

As we can see, unfortunately, at this stage neither of the variables demonstrate the clusters (that are represented in 3 colors) clearly. Meaning there has to be additional work to be put to identify the varying clusters. 

What we can do at this stage is to apply PCA (Principal Component Analysis) that is an algorithm that is used primarily for dimensionality reduction (dimensions meaning variables). This way instead of our initial 19 independent variables and the price (the dependent variable), we can have 2 independent and 1 dependent. Another great outcome of dimensionality reduction is the ability to graph the data. 

![pca_3d_colored.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b5d60bf9-5934-42ba-86d2-3fad18d1dace/pca_3d_colored.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200729T181546Z&X-Amz-Expires=86400&X-Amz-Signature=bf4765a86acf88c751def51e27023013cf6dbe3aed1d4ae54d5ebf1e9d856551&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pca_3d_colored.png%22)

Now, our clusters are more representative and can be easily identified on this plot. However, the problem with PCA and this plot is that even though we can see the clusters now, it is unknown what these newly generated dimensions (namely PCA Variable #1 and PCA Variable #2) represent and thus their practical implementation is limited. 

Lastly, let's try to apply a simple Linear Regression to our model and see if it can accurately guess the price given the variables. 

The linear model produces these two metrics:

> R^2: 0.36123366642285204
Root Mean Squared Error: 91.64320094900793

These two measurements reveal that only 36% of our data fits the model and that on average the price 'guessed' by the model is $91.6 off the real one. 

## Learning Material

Most of the material was learned through the courses provided by the DataCamp platform. These are: 

1) Pandas Foundations 

2) Unsupervised Learning in Python

3) Supervised Learning with scikit-learn 

Also Python Data Science Handbook by Jake Van Der Plas was used for reference.
