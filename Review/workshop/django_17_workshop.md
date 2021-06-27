# django_17_workshop





## Artist List

```python
# http://127.0.0.1:8000/api/v1/artists/

HTTP 200 OK
Allow: GET, POST, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 16,
        "name": "폴킴"
    },
    {
        "id": 17,
        "name": "멜로망스"
    },
    {
        "id": 18,
        "name": "아이유"
    },
    {
        "id": 19,
        "name": "린"
    }
]
```





## Music List

```python
# http://127.0.0.1:8000/api/v1/musics/

HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 11,
        "title": "커피 한 잔 할래요"
    },
    {
        "id": 12,
        "title": "비"
    },
    {
        "id": 13,
        "title": "부끄럼"
    },
    {
        "id": 14,
        "title": "선물"
    },
    {
        "id": 15,
        "title": "내 손을 잡아"
    },
    {
        "id": 16,
        "title": "금요일에 만나요"
    },
    {
        "id": 19,
        "title": "시간을 거슬러"
    }
]
```





## views.py

```python
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

@api_view(['GET', 'DELETE', 'PUT'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'success': True,
            'message': f'deleted artist_id: {artist_pk}',
        }
        return Response(data, status=200)
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = get_list_or_404(Music)
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'success': True,
            'message': f'deleted music_id: {music_pk}',
        }
        return Response(data, status=200)

@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=201)
```





## serializers.py

```python
from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Artist
        fields = '__all__'


class MusicListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Music
        fields = ['id', 'title',]
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta():
        model = Music
        fields = '__all__'
        # read_only_fields = ('artists',)

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    class Meta():
        model = Artist
        fields = '__all__'
```

