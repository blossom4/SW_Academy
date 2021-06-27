from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        # content만
        fields = ['content',]
        # post를 제외하고
        # exclude = ['post',]