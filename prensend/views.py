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

#추천 알고리즘 (상품명, 가격 입력받음)def get_filtered_items(titleArray1, titleArray2, titleArray3, price):
def get_filtered_items(titleArray1, titleArray2, titleArray3, price):
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
    similar_products1 = find_sim_name(products_df, name_sim_sorted_ind, titleArray1, 3)
    print("similar_products1: ", similar_products1[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")

    similar_products2 = find_sim_name(products_df, name_sim_sorted_ind, titleArray2, 3)
    print("similar_products1: ", similar_products2[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")

    similar_products3 = find_sim_name(products_df, name_sim_sorted_ind, titleArray3, 3)
    print("similar_products1: ", similar_products3[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")

    """
    rows = 9
    cols = 7
    similar_products = [[0] * cols] * rows
    
    
    similar_products1 = find_sim_name(products_df, name_sim_sorted_ind, titleArray1, 3)
    print("similar_products1: ", similar_products1[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")
    
    similar_products2 = find_sim_name(products_df, name_sim_sorted_ind, titleArray2, 3)
    print("similar_products2: ", similar_products2[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")
    
    similar_products3 = find_sim_name(products_df, name_sim_sorted_ind, titleArray3, 3)
    print("similar_products3: ", similar_products3[['rank', 'title', 'price', 'image', 'link', 'rate']], "\n")

    print("similar_products1[0]: ", similar_products1[0])
    print("similar_products1[0][1]: ", similar_products1[0][1])
    print("similar_products1[0][1][1]: ", similar_products1[0][1][1])
    
    for i in range(3):
        similar_products[i].append(similar_products1[i])
    
    for i in range(3):
        similar_products[i+3].append(similar_products2[i])
        
    for i in range(3):
        similar_products[i+6].append(similar_products3[i])
    """

    result_list = []

    #유사도 측정 후 유사한 상품들만 가져와서 2차 필터링 진행 (가격)
    if price == '1':
        result_list.append(similar_products1.query("price < 10000").values.tolist()) 
        result_list.append(similar_products2.query("price < 10000").values.tolist()) 
        result_list.append(similar_products3.query("price < 10000").values.tolist()) 

    elif price == '12':
        result_list.append(similar_products1.query("price < 30000").values.tolist())
        result_list.append(similar_products2.query("price < 30000").values.tolist())
        result_list.append(similar_products3.query("price < 30000").values.tolist())

    elif price == '34':
        result_list.append(similar_products1.query("price < 50000").values.tolist())
        result_list.append(similar_products2.query("price < 50000").values.tolist())
        result_list.append(similar_products3.query("price < 50000").values.tolist())

    elif price == '5':
        result_list.append(similar_products1.query("price < 100000").values.tolist())
        result_list.append(similar_products2.query("price < 100000").values.tolist())
        result_list.append(similar_products3.query("price < 100000").values.tolist())

    print("title: ", result_list[0][1][0])
    res_dic = {}; res_list = []
    
    for i in range(len(result_list[0])):
        for k in range(len(result_list[0])):
            res_dic["title"] = str(result_list[i][k][0])
            res_dic["price"] = str(result_list[i][k][1])
            res_dic["image"] = str(result_list[i][k][2])
            res_dic["link"] = str(result_list[i][k][3])
            res_list.append(res_dic)
            res_dic = {}

    print("\n최종 결과: ", res_list, "\n")
    return res_list

def quizinfo_index(request):
    titleArray=[]
    if request.method == 'POST':
        # age = request.POST['search_mode_age']
        price = request.POST.get('search_mode_price')
        #print("====>>>> POST DATA: ", request.POST.getlist('cb[]'))
        
        titleArray = request.POST.getlist('cb[]')
        
        # 사진에 대한 상품명, 콤보박스로부터 가격 가져옴.
        filtered_items = get_filtered_items(titleArray[0], titleArray[1], titleArray[2], price)
        #filtered_items = get_filtered_items(price)

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
