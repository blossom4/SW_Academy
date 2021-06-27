# django_03_homework





## 1. Model 반영하기

> **“Django가 Model에 생긴 변화를 DB에 반영하는 방법”을 뜻하는 용어를 작성하시오.**

migrate



## 2. Model 변경사항 저장하기

```python
class Article(models.Model):
    title = models.CharField(max_lenth=100)
    content = models.TextField()
```

> **위에서 작성한 Model의 변경 사항을 저장하기 위한 명령어를 작성하시오. 이로 인해 생성 된 파일에 대응되는 SQL문을 확인하는 명령어와 출력 결과를 작성하시오.**

```python
python manage.py makemigrations
```



## 3. Python Shell

```python
python
```



## 4. Django Model Field

> **Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오**

- Auto Field
- BoolenField
- BinaryField
- EmailField
- CharField



___



