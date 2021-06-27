from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)




@require_POST
def logout(request):
    auth_logout(request)
    
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def profile(request, pk):
    User = get_user_model()
    user_info = User.objects.get(pk=pk)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)

def follow(request, pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=pk)

    if me == you:
        return redirect('accounts:profile', pk)

    if me in you.followers.all():
        you.followers.remove(me)
    else:
        you.followers.add(me)
    return redirect('accounts:profile', pk)