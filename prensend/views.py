from django.shortcuts import render
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

#def quiz(request):
#    return render(
#        request,
#        'prensend/quiz.html',
#    )

def quizinfo_index(request):
    search_mode_age = request.GET.get('search_mode_age')
    print(search_mode_age)

    if search_mode_age:
        if search_mode_age == '1020':
            age_list = Item.objects.all
        elif search_mode_age == '30':
            age_list = Item.objects.get(1)
        elif search_mode_age == '40':
            age_list = Item.objects.get(2)
        else:
            age_list = Item.objects.get(3)      

    context = {'age_list':age_list}
    return render(
        request,
        'prensend/quiz.html',
        context
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




    