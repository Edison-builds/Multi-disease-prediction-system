from django.urls import path
from . import views

urlpatterns = [
    path('heart', views.heart, name="heart"),
    path('diabetes', views.diabetes, name="diabetes"),
    path('breast', views.breast, name="breast"),
    path('', views.home, name="home"),
    path('heart_data',views.heart_data,name='heart_data'),
    path('diabetes_data',views.diabetes_data,name='diabetes_data'),
    path('breast_data',views.breast_data,name='breast_data'),
    path('heart_table',views.heart_table,name='heart_table'),
    path('diabetes_table',views.diabetes_table,name='diabetes_table'),
    path('breast_table',views.breast_table,name='breast_table'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out')
]
