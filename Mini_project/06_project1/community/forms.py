from django import forms
from .models import Community, Comment

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        exclude = ['user',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

        

