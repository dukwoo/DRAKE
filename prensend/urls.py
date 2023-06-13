from django.urls import path
from . import views

app_name='prensend'

urlpatterns = [
    path('', views.prensend),
    path('recommend/', views.quizinfo_index),
    path('friends/', views.friends),
    path('quiz/', views.quizinfo_index),
    path('calendar/', views.calendar),
    path('mypage/', views.mypage),
]
