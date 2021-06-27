from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, '이미 로그인 되셨습니당😅')
        return redirect('accounts:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.add_message(request, messages.INFO, '로그인 되었습니당😉')
            return redirect('accounts:index')
        messages.add_message(request, messages.ERROR, '로그인에 실패하셨습니당😱')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def index(request):
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    user_info = get_object_or_404(User, username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/profile.html', context)

def delete(request):
    request.user.delete()
    return redirect('accounts:index')

def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '수정완료 되었습니다')
            return redirect('accounts:profile', request.user.username)
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def pw_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST,)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, '비밀번호가 변경되었습니당😊')
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)