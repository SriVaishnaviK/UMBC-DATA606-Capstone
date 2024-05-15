from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import plotly.graph_objs as go
import plotly.express as px
from sklearn.model_selection import cross_val_score
import reverse_geocoder as rg


def home(request):
    return render(request, "home.html")


def predict(request):
    result2 = " "
    if request.method == 'GET' and 'result2' in request.GET:
        result2 = request.GET['result2']

    return render(request, 'predict.html', {'result2': result2})

def result(request):
    df = pd.read_csv(r"C:\Users\kudik\Downloads\Capstone\dataframe_final.csv")
    columnsDrop = ['date', 'yr_renovated', 'location', 'sqft_lot', 'waterfront', 'view' , 'grade' , 'sqft_above' , 'sqft_basement' ,'zipcode' , 'lat' , 'long' , 'sqft_living15' , 'sqft_lot15']
    df = df.drop(columns=columnsDrop)
    remove_outliers = ['price']

    for column in remove_outliers:
        z_scores = stats.zscore(df[column])
        threshold = 3  # threshold for outlier detection
        df = df[(abs(z_scores) < threshold)]
    X = df.drop('price', axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    xgb_regressor = XGBRegressor()

    scores = cross_val_score(xgb_regressor, X_train, y_train, cv=10, scoring='neg_mean_squared_error')
    mean_rmse = np.sqrt(-scores.mean())

    xgb_regressor.fit(X_train, y_train)

    val1 = int(request.GET.get('n1', 0))
    val2 = int(request.GET.get('n2', 0))
    val3 = int(request.GET.get('n3', 0))
    val4 = int(request.GET.get('n4', 0))
    val5 = int(request.GET.get('n5', 0))
    val6 = int(request.GET.get('n6', 0))


    y_pred = xgb_regressor.predict(np.array([val1, val2, val3, val4, val5, val6]).reshape(1, -1))
    y_pred = round(y_pred[0])
    price = "Estimated Price of the House is $"+str(y_pred)




    return render(request, "predict.html", {"result2":price})

