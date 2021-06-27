from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import PostForm, CommentForm
from .models import Post, Hashtag
from django.contrib.auth.decorators import login_required

# Create your views here.
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
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag)
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

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/detail.html', context)


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


def comment_create(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('posts:detail', post.pk)

def like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        # 이미 좋아요 누름
        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
        # 아직 좋아요 누르지 않음
        else:
            post.like_users.add(request.user)
        return redirect('posts:detail', pk)
    return redirect('accounts:login')

def hashtag(request, hashtag_pk):
    tag = get_object_or_404(Hashtag, pk=hashtag_pk)

    context = {
        'tag': tag,
    }
    return render(request, 'posts/hashtag.html', context)