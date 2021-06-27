# django_14_workshop



## FOLLOW

```python
# urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/follow/', views.follow, name='follow'),
]

```

```python
# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
# views.py

def follow(request, pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=pk)

    if me == you:
        return redirect('accounts:profile', pk)

    if me in you.followers.all():
        you.followers.remove(me)
    else:
        you.followers.add(me)
    return redirect('accounts:profile', pk)
```

```html
<!--profile.html-->

{% if user != user_info %}
    {% if user in user_info.followers.all %}
      <a href="{% url 'accounts:follow' user_info.pk %}">UnFollow</a>
    {% else %}
    <a href="{% url 'accounts:follow' user_info.pk %}">Follow</a>
    {% endif %}
  {% endif %}
  <p>following: {{ user_info.followings.count }}명</p>
  <p>follower: {{ user_info.followers.count }}명</p>
```

