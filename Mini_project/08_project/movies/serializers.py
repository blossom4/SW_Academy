from rest_framework import serializers
from .models import Movie, Review, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    review_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta():
        model = Movie
        fields = '__all__'
    

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class ReviewSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta():
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class CommentListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)