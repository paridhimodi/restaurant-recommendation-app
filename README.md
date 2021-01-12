# Zomato-Recommendation-App

In this project I created a web application that can recommend a restaurant based on the restaurant you liked earlier.
I collected the data using **Web-scrapping** from Zomato-Api. I scrapped following features to make a dataset Name of restaurant, It's cuisines, Reviews List, Rating.
Then the data was preprocessed and saved in the csv file. I used the dataset to **train the model** using **cosine similarity**. I deployed my model using the **Flask** framework on Heroku Cloud Platform.

## Demo

![Screenshot (80)](https://user-images.githubusercontent.com/54037847/104320342-3576a780-5508-11eb-9bf4-70948a039665.png)

![Screenshot (81)](https://user-images.githubusercontent.com/54037847/104320349-37d90180-5508-11eb-8de0-3d9cc98fc55a.png)


This app is currently live and can be found at: https://zomato-restaurant-recommender.herokuapp.com/ 

we are going to take following approch:

### 1. problem defination
Problem Build a system capable of recommending a restaurant based on your previous likes and other people with same likes.
A Recommendation System is an information filtering system that seeks to predict the rating a user would give for the item (in this case a restaurant). We can break down the large matrix of ratings from users and items into two smaller matrixes of user-feature and item-feature.



### 2. data
Original data came from the kaggle competition https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/

### 3. Data preprocessing and EDA
### 4. Creating a model
       I buid two models

XGboost
Random Forest
Deployment
For deploying my web application I used Flask framework and deployed it on heroku.
