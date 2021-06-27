# django_01_workshop





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
import random
import requests
# Create your views here.

def lotto(request):
    numbers = range(1, 46)
    pick_numbers = sorted(random.sample(numbers, 6))

    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    res = requests.get(url)
    lotto_info = res.json()

    winners = []
    for i in range(1, 7):
        num = lotto_info[f'drwtNo{i}']
        winners.append(num)
    
    result = len(set(pick_numbers) & set(winners))

    context = {
        'pick_numbers': pick_numbers,
        'winners': winners,
        'result': result,
    }
    return render(request, 'lotto.html', context)
```

___



## 3. templates/lotto.html

```html
{% extends 'base.html' %}

{% block content %}
	<h1 class="my-5">자동생성된 로또 번호입니다.</h1>
	{% for pick_number in pick_numbers %}
		{% if pick_number > 30 %}
			<div class="border rounded-circle d-inline fs-3 bg-danger">{{ pick_number }}</div>
		{% elif pick_number > 20 %}
			<div class="border rounded-circle d-inline fs-3 bg-success">{{ pick_number }}</div>
		{% elif pick_number > 10 %}
			<div class="border rounded-circle d-inline fs-3 bg-primary">{{ pick_number }}</div>
		{% else %}
			<div class="border rounded-circle d-inline fs-3 bg-light">{{ pick_number }}</div>
		{% endif %}
	{% endfor %}
	
	<h1 class="my-5">이번주 당첨 번호입니다.</h1>
	{% for winner in winners %}
		{% if winner > 30 %}
			<div class="border rounded-circle d-inline fs-3 bg-danger">{{ winner }}</div>
		{% elif winner > 20 %}
			<div class="border rounded-circle d-inline fs-3 bg-success">{{ winner }}</div>
		{% elif winner > 10 %}
			<div class="border rounded-circle d-inline fs-3 bg-primary">{{ winner }}</div>
		{% else %}
			<div class="border rounded-circle d-inline fs-3 bg-light">{{ winner }}</div>
		{% endif %}
	{% endfor %}

	<h1>{{ result }}개가 맞았습니다!</h1>
{% endblock content %}
```

___

