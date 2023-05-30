from django.urls import path
from . import views

urlpatterns = [
    path('', views.prensend),
    path('recommend/', views.recommend),
    path('friends/', views.friends),
    path('quiz/', views.productinfo_index),
    path('calendar/', views.calendar),
    path('mypage/', views.mypage),
]