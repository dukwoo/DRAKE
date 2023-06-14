from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'common/signup.html')
    else:
        form = UserCreationForm
        return render(request, 'common/signup.html', {'form':form})