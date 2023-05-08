from django.shortcuts import render


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

def quiz(request):
    return render(
        request,
        'prensend/quiz.html',
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