from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('user', 'review_like')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('user', 'review',)