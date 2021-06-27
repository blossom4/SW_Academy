from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    choiceA = models.CharField(max_length=200)
    choiceB = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=300, blank=True, default='https://data.ac-illust.com/data/thumbnails/2a/2a2127b1c718e4c2c056eddf3b505dc0_t.jpeg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    CHOICES = (
        ('A', 'A'),
        ('B', 'B')
    )
    choice = models.CharField(max_length=200, choices=CHOICES)
    content = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)