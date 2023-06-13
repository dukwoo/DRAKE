from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
def prensend(request):
    return render(
        request,
        'prensend/prensend.html',
    )

def recommend(request):
    return render(
        request,
        'prensend/recommend.html',
    )

def friends(request):
    return render(
        request,
        'prensend/friends.html',
    )

def calendar(request):
    return render(
        request,
        'prensend/calendar.html'
    )

def mypage(request):
    return render(
        request,
        'prensend/mypage.html'
)

def quizinfo_index(request):
    if request.method == 'POST':
        sel = request.POST.get('search_mode')
        print(sel)
        items = Item.objects.all()

    return render (
        request,
        'prensend/quiz.html',
    )
