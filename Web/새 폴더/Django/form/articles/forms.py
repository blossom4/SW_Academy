from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    # yesorno = forms.BooleanField()
    # due_date = forms.DateTimeField()
    # location = forms.ChoiceField()

class ArticleModelForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'