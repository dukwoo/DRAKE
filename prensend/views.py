import json
import random

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Item
from .models import Item_csv

from django.core import serializers

import pandas as pd
import numpy as np
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models.query import QuerySet

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
    
def login(request):
    return render(
        request,
        'prensend/login.html'
    )

#head가 안되어서 상위 3개만 읽어오는 함수 만들어봄
def get_top_n(list_a, num):
    '''
    list_a: [int, int, ...]
    num: int, 추출하고 싶은 개수
    '''
    tmp = list_a.copy()
    tmp.sort()
    
    top_num = tmp[-num:]  # 뒤에서부터 추출
    top_idx = [list_a.index(x) for x in top_num]


    return top_idx

def find_sim_name(df, sorted_ind, product_name, top_n=3):
        #인자로 입력된 products_df DataFrame에서 'title' 칼럼이 입력된 product_name 값인 DataFrame 추출
        title_product = df[df['title'] == product_name]

        #product_name을 가진 DataFrame의 index 객체를 ndarray로 반환하고
        #sorted_ind 인자로 입력된 name_sim_sorted_ind 객체에서 유사도 순으로 top_n개의 index 추출
        title_index = title_product.index.values
        print("title_index: ", title_index, "\n")
        similar_indexes = sorted_ind[title_index, :(top_n)]

        #추출된 top_n index 출력. top_n idnex는 2차원 데이터.
        #DataFrame 에서 index로 사용하기 위해선 1차원 array로 변경
        print("similar_indexes : ", similar_indexes, "\n")
        similar_indexes = similar_indexes.reshape(-1)

        return df.iloc[similar_indexes]

#추천 알고리즘 (상품명, 가격 입력받음)
def get_filtered_items(price):
    #2
    warnings.filterwarnings('ignore')

    #items = pd.read_csv('product.csv', engine = 'python', encoding='cp949') #'euc-kr'
    items = Item.objects.all()
    products_df = pd.DataFrame(items.values('rank', 'title', 'price', 'image', 'link', 'rate'))
    #products_df = items[['title', 'price', 'category']]
    

    #매트릭스의 형태를 상품수, 상품명
    #CountVectorizer를 적용하기 위해 공백문자로 word 단위가 구분되는 문자열로 반환
    #상품명을 공백으로 나눠서 각각의 단어의 개수를 추출.
    #3
    products_df['title_literal'] = products_df['title'].apply(lambda x:('').join(x))
    count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
    name_mat = count_vect.fit_transform(products_df['title_literal'])
    print("name_mat.shape : ", name_mat.shape, "\n")

    name_sim = cosine_similarity(name_mat, name_mat)
    print("name_sim.shape :", name_sim.shape, "\n")
    print("name_sim[:1] : ", name_sim[:1], "\n")

    name_sim_sorted_ind = name_sim.argsort()[:, ::-1]
    print("name_sim_sorted_ind[:1] : ", name_sim_sorted_ind[:1], "\n")

    #유사한 상품들 가져옴
    similar_products = find_sim_name(products_df, name_sim_sorted_ind, '나이키 기능성 드라이핏 반팔 긴팔티 프로 컴프레션', 3)
    print("similar_products: ", similar_products[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")

    result_list = []
    result_list.append(similar_products.query("price < 100000").values.tolist())

    print("title: ", result_list[0][1][0])

    result_dic = {}

    result_dic["title"] = str(result_list[0][1][1])
    result_dic["price"] = str(result_list[0][1][2])
    result_dic["image"] = str(result_list[0][1][3])
    result_dic["link"] = str(result_list[0][1][4])

    print(result_dic)
    return result_dic

    # 유사도 측정 후 유사한 상품들만 가져와서 2차 필터링 진행 (가격)
    """
    #result_list=[];
    
    if price == '1':
        result_list.append(similar_products.query("price < 10000").values.tolist()) 

    elif price == '12':
        result_list.append(similar_products.query("price < 30000").values.tolist())

    elif price == '34':
        result_list.append(similar_products.query("price < 50000").values.tolist())

    elif price == '5':
        result_list.append(similar_products.query("price < 100000").values.tolist())
    """

    #numpy_ba = similar_products.to_numpy()

    #result_list2.append(result_list[0][1])
    #print(result_list2)

    """
    #데이터프레임을 json으로 변환
    json_data = similar_products.to_json(orient='records')

    print("json_data : " , json_data , "\n")
    #여기까진 잘됨
    """



    """
    retItems = {}
    i = 0
    for item in json_data["items"]["item"]:
        item = dict(item.items())
        retItems['item' + str(i)] = (json.dumps(item, ensure_ascii=False))
        i += 1
        # make dict_items type Objects to list type objects

        # return datas to json data
    """



    #json을 쿼리셋으로 변환
    #queryset = serializers.deserialize('json', json_data)
    #mylist = list(queryset)
    #dataframe을 queryset으로 변환해야함.
    #print("넘피배열 : ", numpy_ba, "\n")
    #return numpy_ba

def quizinfo_index(request):
    if request.method == 'POST':
        # age = request.POST['search_mode_age']
        price = request.POST.get('search_mode_price')

        # 사진에 대한 상품명, 콤보박스로부터 가격 가져옴.
        filtered_items = get_filtered_items(price)

        context = {
            'filtered_items': filtered_items,
        }

        return render(request, 'prensend/recommend.html', context)

def quiz(request):
    itemsAll = list(Item.objects.all())
    items = random.sample(itemsAll, 12)
    
    context = {'items':items}
    
    
    return render(
        request,
        'prensend/quiz.html',
        context
    )
