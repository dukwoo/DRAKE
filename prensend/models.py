from django.db import models
from django import forms
from django.contrib.auth.models import User
import os

class Clue(models.Model):
    #단서id
    clueid = models.IntegerField(default=0)
    #사용자id
    userid = models.IntegerField(default=0)
    #단서명
    cluename = models.CharField(max_length=100)

    def __str__(self):
        return f'단서id :{self.clueid} \n 사용자id :{self.userid} \n 단서명 :{self.cluename} \n'
    

class Item(models.Model):
    #순위
    #rank = models.CharField(max_length=10, blank=True)
    rank = models.IntegerField(default=0)
    #상품명
    title = models.CharField(max_length=100)
    #가격
    price = models.IntegerField(default=0)
    #이미지 (frensend)
    image = models.ImageField(upload_to='prensend/images/%Y/%m/%d/', blank=True)
    #링크
    link = models.CharField(max_length=300, blank=True)
    #별점
    rate = models.FloatField(default=0.0)


    def __str__(self):
        return f'[{self.pk}] [{self.rank}위] 상품명 :{self.title} \n 가격 :{self.price} \n 이미지 링크 :{self.image} \n 링크 :{self.link} \n 평점: {self.rate} \n\n'

    def get_absolute_url(self):
        return f'/prensend/{self.pk}/'

class Item_csv(models.Model):
    # 순위
    rank = models.CharField(max_length=10, blank=True)
    # 상품명
    title = models.CharField(max_length=100)
    # 가격
    price = models.CharField(max_length=30, blank=True)
    # 이미지 (frensend)
    image = models.CharField(max_length=300, blank=True)
    # 링크
    link = models.CharField(max_length=300, blank=True)
    # 카테고리
    category = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.rank + "위 \n 상품명:" + self.title + "\n" + self.price + "원 \n" + self.image + "," + self.link + "," + self.category

'''
class FilterForm(forms.Form):
    category_choices = [(category, category) for category in Item.objects.values_list('category', flat=True).distinct()]
    category = forms.ChoiceField(choices=category_choices)
    # 필요한 추가 필드들을 정의합니다.


class FilterItem(models.Model):
    gender_Choices = (('여자','여자'), ('남자', '남자'))
    gender = models.CharField(max_length=10, choices=gender_Choices)

    age_Choices = (('10-20대', '10-20대'), ('30대', '30대'), ('40대', '40대'), ('50대', '50대'))
    age = models.CharField(max_length=20, choices=age_Choices)

    price_Choices = (('1만원 이하', '1만원 이하'), ('1-2만원', '1-2만원'), ('3-4만원', '3-4만원'), ('5-6만원', '5-6만원'))
    price = models.CharField(max_length=20, choices=price_Choices)

'''