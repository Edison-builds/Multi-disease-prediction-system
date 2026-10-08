from django.shortcuts import render, redirect
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
from predictor.forms import BreastCancerForm, DiabetesForm, HeartDiseaseForm
import csv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core import settings
import os


def heart(request):
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]
    value = ''
    if request.method == 'POST':
        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        data = rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)
        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"

    return render(request,
                  'heart.html',
                  {
                      'a':data,
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': HeartDiseaseForm(),
                  })


def diabetes(request):

    dfx = pd.read_csv('static/Diabetes_XTrain.csv')
    dfy = pd.read_csv('static/Diabetes_YTrain.csv')

    # Remove unwanted extra column
    dfx = dfx.loc[:, ~dfx.columns.str.contains('^Unnamed')]

    # Ensure training features exclude the outcome label column if present
    if 'Outcome' in dfx.columns:
        X = dfx.drop(columns=['Outcome']).values
    else:
        X = dfx.values

    Y = dfy.values.reshape((-1,))

    value = ''

    if request.method == 'POST':

        pregnancies = float(request.POST['pregnancies'])
        glucose = float(request.POST['glucose'])
        bloodpressure = float(request.POST['bloodpressure'])
        skinthickness = float(request.POST['skinthickness'])
        bmi = float(request.POST['bmi'])
        insulin = float(request.POST['insulin'])
        pedigree = float(request.POST['pedigree'])
        age = float(request.POST['age'])

        user_data = np.array([
            pregnancies,
            glucose,
            bloodpressure,
            skinthickness,
            bmi,
            insulin,
            pedigree,
            age
        ]).reshape(1, -1)

        print(user_data.shape)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X, Y)

        predictions = knn.predict(user_data)

        if int(predictions[0]) == 1:
            value = 'have'
        else:
            value = "don't have"

    return render(request, 'diabetes.html', {
        'result': value,
        'title': 'Diabetes Disease Prediction',
        'active': 'btn btn-success peach-gradient text-white',
        'diabetes': True,
        'form': DiabetesForm(),
    })


def breast(request):
    df = pd.read_csv('static/Breast_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    print(X.shape, Y.shape)

    value = ''
    if request.method == 'POST':

        radius = float(request.POST['radius'])
        texture = float(request.POST['texture'])
        perimeter = float(request.POST['perimeter'])
        area = float(request.POST['area'])
        smoothness = float(request.POST['smoothness'])

        """ 
        21:02:21 09 Oct, 2019 by Arjun Adhikari
        Creating our training model. 
        """
        rf = RandomForestClassifier(
            n_estimators=16, criterion='entropy', max_depth=5)
        rf.fit(np.nan_to_num(X), Y)

        user_data = np.array(
            (radius,
             texture,
             perimeter,
             area,
             smoothness)
        ).reshape(1, 5)
        predictions = rf.predict(user_data)
        print(predictions)
        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"

    return render(request,
                  'breast.html',
                  {
                      'result': value,
                      'title': 'Breast Cancer Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'breast': True,
                      'form': BreastCancerForm(),
                  })
def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
    return data


def home(request):
    return render(request,'home.html')


def log_in(request):
    if request.method == 'POST':
        us = request.POST.get('username')
        pws = request.POST.get('password')
        user = authenticate(request,username=us,password=pws)
        if user is not None:
            login(request,user)
        return redirect('heart_table')
    return render(request,'log_in.html')



def log_out(request):
    logout(request)
    return redirect('home')


def heart_table(request):
    data = read_csv(r'C:\Users\ediso\OneDrive\Desktop\MULTI DISEASE\Source Code\static\Heart_train.csv')
    return render(request,'heart_table.html',{'data':data})

def diabetes_table(request):
    data = read_csv(r'C:\Users\ediso\OneDrive\Desktop\MULTI DISEASE\Source Code\static\Diabetes_XTrain.csv')
    return render(request,'diabetes_table.html',{'data':data})

def breast_table(request):
    data = read_csv(r'C:\Users\ediso\OneDrive\Desktop\MULTI DISEASE\Source Code\static\Breast_train.csv')
    return render(request,'breast_table.html',{'data':data})


def heart_data(request):
    qwerty = pd.read_csv('static/Heart_train.csv')
    qwerty.tail()
    qwerty.describe()
    qwerty.select_dtypes('int')
    qwerty.select_dtypes(exclude= int)
    qwerty.describe().T
    qwerty.sample(10)
    qwerty.isnull().sum()
    qwerty.dropna(inplace = True)
    qwerty.nunique()
    fig = px.scatter(qwerty, x="age", y="trestbps", color="target", title="Age vs Blood Pressure")
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    fig1 = px.scatter(qwerty, x="chol", y="slope", color="target", title="Chol vs Slope")
    plot_html1 = fig1.to_html(full_html=False, include_plotlyjs=False)
    return render(request,'heart_data.html',{'plot_html':plot_html,'plot_html1':plot_html1})



def diabetes_data(request):
    qwerty = pd.read_csv('static/Diabetes_XTrain.csv')
    qwerty.tail()
    qwerty.describe()
    qwerty.select_dtypes('int')
    qwerty.select_dtypes(exclude= int)
    qwerty.describe().T
    qwerty.sample(10)
    qwerty.isnull().sum()
    qwerty.dropna(inplace = True)
    qwerty.nunique()
    fig = px.scatter(qwerty, x="Age", y="BMI", color="Outcome", title="Age vs Body Mass Index")
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    fig1 = px.scatter(qwerty, x="BloodPressure", y="Glucose", color="Outcome", title="BloodPressure vs Glucose")
    plot_html1 = fig1.to_html(full_html=False, include_plotlyjs=False)
    return render(request,'diabetes_data.html',{'plot_html':plot_html,'plot_html1':plot_html1})


def breast_data(request):
    qwerty = pd.read_csv('static/Breast_train.csv')
    qwerty.tail()
    qwerty.describe()
    qwerty.select_dtypes('int')
    qwerty.select_dtypes(exclude= int)
    qwerty.describe().T
    qwerty.sample(10)
    qwerty.isnull().sum()
    qwerty.dropna(inplace = True)
    qwerty.nunique()
    fig = px.scatter(qwerty, x="mean_area", y="mean_texture", color="diagnosis", title="Mean area vs Mean Texture ")
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    fig1 = px.scatter(qwerty, x="mean_radius", y="mean_perimeter", color="diagnosis", title="Mean radius vs Mean Perimeter")
    plot_html1 = fig1.to_html(full_html=False, include_plotlyjs=False)
    return render(request,'breast_data.html',{'plot_html':plot_html,'plot_html1':plot_html1})


def handler404(request):
    return render(request, '404.html', status=404)
