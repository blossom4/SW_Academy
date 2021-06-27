# django_08_workshop





## 1. /accounts/

> **유저 목록을 출력하는 페이지를 나타낸다.**

```python
# urls.py
urlpatterns = [
    path('', views.index, name='index'),
]
```

```python
# views.py
def index(request):
    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)
```

```html
<!--index.html-->
{% extends 'base.html' %}

{% block content %}
  <h1>User List</h1>
  {% for user in users %}
    <p>{{ user }}</p>
  {% endfor %}
{% endblock content %}
```





## 2. /accounts/signup/

> **회원가입 작성을 위한 페이지를 나타낸다. 유저를 생성하는 기능을 수행한다.**

```python
# urls.py
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```python
# views.py
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)
```

```html
<!--form.html-->
{% extends 'base.html' %}

{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
	<input type="submit">
  </form>
{% endblock content %}
```



___

