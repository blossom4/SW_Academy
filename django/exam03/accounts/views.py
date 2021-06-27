from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

# Create your views here.
def signup(request):
    # Q1-1
    # 이미 로그인한 유저라면 index페이지로 redirect해준다.
    if request.user.is_authenticated:
        return redirect('reservations:index')
    # 1. POST 방식으로 정보가 온것이 아니면, 만들어둔 form을 불러와서 보여준다.
    # 2. POST방식으로 정보가 입력되면, 만들어둔 form을 불러와서 유효성 검사후  입력받은 데이터를 저장.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
    

def login(request):
    # Q1-2
    # 이미 로그인 되어있다면 index페이지로 보내준다.
    if request.user.is_authenticated:
        return redirect('reservations:index')
    # 1. POST 방식으로 정보가 온것이 아니면, 만들어둔 form을 불러와서 보여준다.
    # 2. POST방식으로 정보가 입력되면, 만들어둔 form을 불러와서 유효성 검사후  입력받은 데이터를 저장.
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reservations:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
   

def logout(request):
    # Q1-3
    auth_logout(request)
    return redirect('accounts:login')
    