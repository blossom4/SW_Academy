# django_09_homework



## 1. User Model BooleanField

> ** 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField 로 정의 된 컬럼을 모두 작성하시오.**

```python
is_staff
is_active
is_superuser
```



## 2. username max length

> **django에서 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길이를 작성하시오.**

```python
 username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
```

```python
150max_length=150
```





## 3. login validation

> **단순히 사용자가 ‘로그인 된 사용자인지’만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.**

```python
 @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
```



## 4. Login 기능 구현

> **다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.**

```python
from django.contrib.auth.forms import __(a)__
from django.contrib.auth import __(b)__ as auth_login

def login(request):
    if request.method == 'POST':
        form = __(a)__(request, request.POST)
        if form.is_vaild():
            auth_login(request, __(c)__)
            return redirect('accounts:index')
    else:
        form = __(a)__()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

```python
(a): AuthenticationForm
(b): login
(c): form.get_user()
```





## 5. who are you?

> **로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.**

```python
class AnonymousUser:
    id = None
    pk = None
    username = ''
    is_staff = False
    is_active = False
    is_superuser = False
    _groups = EmptyManager(Group)
    _user_permissions = EmptyManager(Permission)
```





## 6. 암호화 알고리즘

> **Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 작성하시오.**

```python
password 저장에 사용하는 알고리즘 : pbkdf22
함꼐 사용된 해시 함수 : sha256
```





## 7. Logout 기능 구현

> **로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오**

```python
def logout(request):
    logout(request)
    return redirect('accounts:login')
```

```python
이름이 중복이 되었기 때문에 재귀적으로 자기자신을 호출하게 되서 문제가 발생한다. 따라서 logout을 auth_logout과 같이 바꾸면 된다.
```



___

