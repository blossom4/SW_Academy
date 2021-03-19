from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie
from .forms import MovieForm

@require_safe
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method =='POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save()

            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    
    context = {
        'form': form,
    }

    return render(request, 'movies/form.html', context)


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)

    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
    }

    return render(request, 'movies/form.html', context)


@require_POST
def delete(requset, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()

    return redirect('movies:index')
    