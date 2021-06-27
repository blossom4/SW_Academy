# django_12_workshop



## LIKE

```python
# urls.py

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/like/', views.like, name='like'),
]
```

```python
# models.py

from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
```

```python
# views.py

def like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        # 이미 좋아요 누름
        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
        # 아직 좋아요 누르지 않음
        else:
            post.like_users.add(request.user)
        return redirect('posts:detail', pk)
    return redirect('accounts:login')
```

```html
<!--detail.html-->

{% if request.user in post.like_users.all %}
  <a href="{% url 'posts:like' post.pk %}">💗</a>
{% else %}
  <a href="{% url 'posts:like' post.pk %}">🤍</a>
{% endif %}
```





