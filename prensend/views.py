from django.db.models import Q
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

def get_filtered_items(age, gender, price):
    items = Item.objects.all()
    result_list = []

    if age == '1020' & gender == 'man' & price == '1':
        result_list.append(items.objects.filter(Q(category='20M') & Q(price__lte = 10000)).order_by('rank'))
        #카테고리가 20M 이어야하고 price가 10000이하인걸

    elif age == '1020' & gender == 'man' & price == '12':
        result_list.append(items.objects.filter(Q(category='20M') & Q(price__gt = 10000) & Q(price__lt = 30000)).order_by('rank'))

    elif age == '1020' & gender == 'man' & price == '34':
        result_list.append(items.objects.filter(Q(category='20M') & Q(price__gte = 30000) & Q(price__lt = 50000)).order_by('rank'))

    elif age == '1020' & gender == 'man' & price == '5':
        result_list.append(items.objects.filter(Q(category='20M') & Q(price__gte = 50000)).order_by('rank'))

    return result_list


def quizinfo_index(request):

    if request.method == 'POST':
        age = request.POST.get('search_mode_age')
        gender = request.POST.get('search_mode_gender')
        price = request.POST.get('search_mode_price')

        filtered_items = get_filtered_items(age, gender, price)

        context = {
            'filtered_items': filtered_items,
        }
        return render(request, 'prensend/recommend.html', context)

    return render(request, 'prensend/quiz.html')