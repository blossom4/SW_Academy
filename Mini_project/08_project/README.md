# README



```python
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
```

![Movie_list](C:\Users\cho82\Desktop\Movie_list.PNG)



___

```python
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

![Movie_detail](C:\Users\cho82\Desktop\Movie_detail.PNG)

___

```python
@api_view(['GET', 'POST'])
def review_list(request, movie_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
```

> ![Review_list](C:\Users\cho82\Desktop\Review_list.PNG)



___



```python
@api_view(['GET', 'PUT', 'DELETE'])
def reivew_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'success': True,
            'deleted_review_pk': review_pk,
        }
        return Response(data, status=200)
```

![Review_detail](C:\Users\cho82\Desktop\Review_detail.PNG)





```python
@api_view(['POST'])
def comment_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=200)
```

![Comments_create](C:\Users\cho82\Desktop\Comments_create.PNG)