from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

@require_safe
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    form =CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
    else:
        return redirect('accounts:login')
    return redirect('posts:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def comment_create(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return redirect('posts:detail', post.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    else:
        return redirect('accounts:login')
    return redirect('posts:detail', pk)