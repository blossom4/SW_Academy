# django_07_homework



## 1. Compiled Bootstrap

> **CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오. 부트스트랩이 적용되기 위해 작성해야 할 코드를 제출하시오.**

```python
# settings.py
INSTALLED_APPS = [
    'bootstrap5',
]
```

```html
<!--base.html-->
<link rel="stylesheet" href="{% static 'bootstrap.css' %}">
<script src="{% static 'bootstrap.js' %}"></script>
```

```html
<!--___.html-->
{% load bootstrap5 %}
```



___





