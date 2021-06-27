from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# class Profile(models.Model):
#     # user라는 모델을 만들면 profile은 하나만 붙을 수 있다.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
