# django_09_workshop





## 1. User Change Password

> **/accounts/password/ url을 가지며 유저의 비밀번호 수정 기능을 구현한다**

```python
# urls.py
urlpatterns = [
    path('password/', views.pw_update, name='pw_update'),
]
```

```python
# views.py
def pw_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST,)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, '비밀번호가 변경되었습니다.')
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
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

