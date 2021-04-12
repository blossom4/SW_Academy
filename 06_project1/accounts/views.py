from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def signup(request): 
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == "POST": 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = { 
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else: 
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')

def profile(request, pk):
    User = get_user_model()
    user_info = User.objects.get(pk=pk)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)