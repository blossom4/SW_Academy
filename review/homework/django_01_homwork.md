# django_01_homwork



## 1. 한국어로 번역하기

> 1-1. django 프로젝트를 한국어로 제공하기 위해 번역이 필요하다. 이 설정을 위해 settings.py에 어떤 변수 그리고 어떤 값을 할당해야 하는지 작성하시오.

LANGUAGE_CODE



> 1-2 추가로 settings.py에 ‘이 변수‘가 활성화인 상태여야 1-1번 변수를 설정할 수 있다고 한 다. ‘이 변수’는 무엇인가?’





___

## 2.  경로 설정하기

> 다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오.

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path(__(a)__),
    path('admin/', admin.site.urls),
]
>>
path('ssafy/', ssafy.views.urls name='ssafy'),
```



3-1 menu

3-2 forloop.counter[number - 1]

3-3 empty

3-4 if / else

3-5 length

3-6 title





1)  form ~로 ~를 action '보낸다'

2) GET / POST



3) /create/?title=안녕하세요/content=반갑습니다/my-site=파이팅/