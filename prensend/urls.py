from django.urls import path
from . import views

app_name = 'prensend'

urlpatterns = [
    path('', views.prensend),
    path('recommend/', views.quizinfo_index, name='quizinfo_index'),
    path('friends/', views.friends),
    path('quiz/', views.quiz),
    path('calendar/', views.calendar),
    path('mypage/', views.mypage),
    path('login/', views.login),
]
