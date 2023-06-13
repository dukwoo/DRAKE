from django import forms
from .models import Item, FilterItem


class QuestionForm(forms.ModelForm):
    class Meta:
        model = FilterItem
        fields = ('gender','age','price')

        widgets = {
            'gender' : forms.TextInput(attrs={'class': 'form-control'}),
            'age' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
        }

    # 사용할 모델 fields = ['subject', 'content']
    # QuestionForm에서 사용할 Question 모델의 속성