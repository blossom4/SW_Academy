from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
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
import random as get_random

# Create your views here.

def home(request):
    return render(request, 'posts/home.html')

def index(request):
    posts = Post.objects.all()[::-1]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def random(request):
    posts = Post.objects.all()
    post = get_random.choice(posts)
    return redirect('posts:detail', post.pk)



def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by('-pk')
    comments_a = comments.filter(choice='A')
    count_a = comments_a.count()
    count_b = comments.count() - comments_a.count()
    if comments:
        percent_a = round((comments_a.count() / comments.count()) * 100, 2)
        percent_b = 100 - percent_a
    else:
        percent_a = 0
        percent_b = 0
    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'count_a': count_a,
        'count_b': count_b,
        'percent_a': percent_a,
        'percent_b': percent_b,
    }
    return render(request, 'posts/detail.html', context)

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated😀')
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:index')

def comment_create(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', post.pk)
    else:
        messages.info(request, '로그인 해주세요')
        return redirect('posts:detail', post.pk)

def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    else:
        return redirect('accounts:login')
    return redirect('posts:detail', pk)