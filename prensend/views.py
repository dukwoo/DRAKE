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

'''
def productinfo_index(request):

    #오름차순으로 1등부터 가져오기 
    products = Item.objects.all()

    #필터 함수
    def is_20man(products):
        return products["category"] == "20M"
    
    def is_20woman(products):
        return products["category"] == "20W"

    def is_30man(products):
        return products["category"] == "30M"
    
    def is_30woman(products):
        return products["category"] == "30W"

    def is_40man(products):
        return products["category"] == "40M"
    
    def is_40woman(products):
        return products["category"] == "40W"

    def is_50man(products):
        return products["category"] == "50M"
    
    def is_50woman(products):
        return products["category"] == "50W"

    #입력 인자 (나이, 성별, 가격)
    search_mode_age = request.GET.get('search_mode_age')
    search_mode_price = request.GET.get('search_mode_price')
    search_mode_gender = request.GET.get('search_mode_gender')
    print(search_mode_age,",",search_mode_price,",",search_mode_gender)

    #나이 성별 확인
    if search_mode_age and search_mode_gender:
        if search_mode_age == '1020':
            if search_mode_gender == 'man':
                product_list = products.filter(is_20man, products)
            elif search_mode_gender == 'woman':
                product_list = products.filter(is_20woman, products)
       
        elif search_mode_age == '30':
            if search_mode_gender == 'man':
                product_list = products.filter(is_30man, products)
            elif search_mode_gender == 'woman':
                product_list = products.filter(is_30woman, products)

        elif search_mode_age == '40':
            if search_mode_gender == 'man':
                product_list = products.filter(is_40man, products)
            elif search_mode_gender == 'woman':
                product_list = products.filter(is_40woman, products)

        elif search_mode_age == '50':
            if search_mode_gender == 'man':
                product_list = products.filter(is_50man, products)
            elif search_mode_gender == 'woman':
                product_list = products.filter(is_50woman, products)
    
    context = {'product_list':product_list}
    return render(request, 'prensend/quiz.html', context)
'''




    