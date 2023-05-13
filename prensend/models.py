from django.db import models
from django.contrib.auth.models import User
import os


class Item(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    price = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return f'/prensend/{self.pk}/'
