# django_10_homework





## 1. Lookup

> **지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오. **
>
> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups



```python
Entry.objects.filter(pk__gt=4)
```





## 2. 1:N 관계 설정

> **지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오. **
>
> **https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments**

```python
class Comment(models.Model):
    content = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=__(a)__)
```

CASCADE:

SET_DEFAULT: 유저가 삭제가되면 새로운 값을 참조하여 비지 않도록해준다.

DO_NOTHING: 아무것도 하지 않는다.





## 3. comment create view

> **지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.**

```python
def comment_create(request, pk):
    Article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(__(a)__)
            comment.article = article
            comment.save()
            return redirect('articles:index')
```

```python
(a): commit=FALSE
```







## 4. 1:N DB API

> **게시물 아래에 댓글을 출력하려고 한다. Article과 Comment 모델이 1:N으로 관계설정 이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.**

```html
<h1>{{ article.title }}</h1>
{% for comment in __(a)__ %}
  <p>{{ comment.content }}</p>
{% empty %}
  <p>댓글이 없습니다.</p>
{% endfor %}
```

```python
(a): article.comment_set.all
```









___

