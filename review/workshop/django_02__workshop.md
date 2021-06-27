# django_02__workshop



## 1. intro/urls.py

```python
"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
]
```

___



## 2. pages/views.py

```python
from django.shortcuts import render
import requests
# Create your views here.

def dinner(request, menu, number):

    context = {
        'menu': menu,
        'number': number,
    }
    return render(request, 'dinner.html', context)
```

___



## 3. templates/dinner.html

```html
{% extends 'base.html' %}

{% block content %}
	메뉴 : {{ menu }}
	몇명 : {{ number }}
{% endblock content %}
```

___

