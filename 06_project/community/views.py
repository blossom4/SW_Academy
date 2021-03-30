from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommunityForm, CommentForm
from .models import Community

# Create your views here.
def index(request):
    reviews = Community.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/index.html', context)


def create(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            form = CommunityForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('community:detail', review.pk)
        else: 
            form = CommunityForm()
        context = {
            'form': form, 
        }
        return render(request, 'community/form.html', context)
    else:
        return redirect('community:index')


def detail(request, review_pk):
    review = get_object_or_404(Community, pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review, 
        'comment_form': comment_form, 
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


def create_comments(request, review_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            review = get_object_or_404(Community, pk=review_pk)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.review = review
                comment.save()
                return redirect('community:detail', review.pk)
            context = {
                'comment_form': comment_form, 
                'review': review, 
            }
            return render(request, 'community/detail.html', context)
    else: 
        return redirect('accounts:login')