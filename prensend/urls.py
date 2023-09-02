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
    path('game/', views.game),
    path('modal/', views.modal),
    path('gamerecommend/', views.quizinfo_index_game, name='quizinfo_index_game'),
    path('gamerecommend2/', views.quizinfo_index_game2, name='quizinfo_index_game2'),
    path('gamerecommend3/', views.quizinfo_index_game3, name='quizinfo_index_game3'),
    path('gamerecommend4/', views.quizinfo_index_game4, name='quizinfo_index_game4'),
]
