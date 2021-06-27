# django_15_workshop





## HASH_TAG

```python
# urls.py

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('hashtags/<int:hashtag_pk>/', views.hashtag, name='hashtag')
]
```

```python
# models.py

from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)
```

```python
# views.py

def hashtag(request, hashtag_pk):
    tag = get_object_or_404(Hashtag, pk=hashtag_pk)

    context = {
        'tag': tag,
    }
    return render(request, 'posts/hashtag.html', context)
```

```html
<!--_card.html-->

<p class="card-text">{{ post|hashtag_link|safe }}</p>
```

```html
<!--hashtag.html-->

{% extends 'base.html' %}

{% block content %}

<h1>{{ tag.content }}</h1>
<div class="row row-cols-1 row-cols-md-3 g-4">
    {% for post in tag.posts.all %}
      <div class="col">
        {% include 'posts/_card.html' %}
      </div>
    {% endfor %}
  </div>
{% endblock content %}
```



