from django.db import models
from django.contrib.auth.models import User
import os


class Item(models.Model):
    #순위
    rank = models.CharField(max_length=10, blank=True)
    #상품명
    title = models.CharField(max_length=100)
    #가격
    price = models.CharField(max_length=30, blank=True)
    #이미지 (frensend)
    image = models.ImageField(upload_to='prensend/images/%Y/%m/%d/', blank=True)
    #링크
    link = models.CharField(max_length=300, blank=True)
    #카테고리
    category = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'[{self.pk}] : {self.title}'

    def get_absolute_url(self):
        return f'/prensend/{self.pk}/'
