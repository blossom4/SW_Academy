from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # read_only 가 있어야 is_valid를 문제없이 통과할 수 있다.
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 해당 article 번호의 댓글id만 보내줌
    comment_set = CommentSerializer(many=True, read_only=True) # 해당 article 번호와 내용들까지 다 보내줌
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta():
        model = Article
        fields = '__all__'