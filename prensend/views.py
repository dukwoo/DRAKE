from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Item
from .models import Item_csv

# Create your views here.
def prensend(request):
    return render(
        request,
        'prensend/prensend.html',
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

#추천 알고리즘 (상위 3개만 가져오기, 상품명, 가격, 이미지, 링크 다 따로따로 리스트 만들어서 가져와야하나?)
def get_filtered_items(age, gender, price):
    items = Item.objects.all()
    result_list = []

    s_age = '20M'
    if(age == '1020') & (gender == 'man'):
        s_age = '20M'
    elif (age == '1020') & (gender == 'woman'):
        s_age = '20W'
    elif (age == '30') & (gender == 'man'):
        s_age = '30M'
    elif(age == '30') & (gender == 'woman'):
        s_age = '30W'
    elif (age == '40') & (gender == 'man'):
        s_age = '40M'
    elif (age == '40') & (gender == 'woman'):
        s_age = '40W'
    elif (age == '50') & (gender == 'man'):
        s_age = '50M'
    elif (age == '50') & (gender == 'woman'):
        s_age = '50W'


    if price == '1':
        result_list.append(items.filter(Q(category=s_age) & Q(price__lte = 10000)).order_by('rank'))
        #카테고리가 20M 이어야하고 price가 10000이하인걸

    elif price == '12':
        result_list.append(items.filter(Q(category=s_age) & Q(price__gt = 10000) & Q(price__lt = 30000)).order_by('rank'))

    elif price == '34':
        result_list.append(items.filter(Q(category=s_age) & Q(price__gte = 30000) & Q(price__lt = 50000)).order_by('rank'))

    elif price == '5':
        result_list.append(items.filter(Q(category=s_age) & Q(price__gte = 50000)).order_by('rank'))

    return result_list

    #현재 문제점 : 추천 알고리즘 완성, 이부분은 교수님 피셜 문제없다고 확인받음 -> 문제는 필터링된 데이터 리스트에서 상위 3개를 뽑는 것 (head쓰면 오류남), 리스트에는 필터링된 아이템들이 다 담겨있음.
    # 앞선 상위 3개 뽑는 것이 되지 않아서 상위 3개 데이터를 recommend 페이지에서 보이게 하는 것이 안됨 -> 이부분에서 아이템을 읽어오지 못하는 것 같음
    # 모델에서 Char 형식으로 rank를 입력받아 order by를 rank로 하지 못하는 것이 의심됨 -> 그러나 Int 형식으로 모델 수정하면 오류남.
    # result_list의 내용을 확인해보고 싶은데 print 작동안함

def quizinfo_index(request):
    if request.method == 'POST':
        age = request.POST.get('search_mode_age')
        # age = request.POST['search_mode_age']
        gender = request.POST.get('search_mode_gender')
        price = request.POST.get('search_mode_price')

        filtered_items = get_filtered_items(age, gender, price)

        context = {
            'filtered_items': filtered_items,
        }
        return render(request, 'prensend/recommend.html', context)

def quiz(request):
    return render(
        request,
        'prensend/quiz.html',
    )