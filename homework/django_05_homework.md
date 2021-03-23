# django_05_homework



```python
from django.shortcuts import render, redirect
from .forms import ArticlesForm

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirct('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



> **1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?**

```python
어떤 방식으로 요청이 들어와도 마지막에 context로 받아서 처리해주기 위해서이다.
```



> **2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?**

```python
변경된 사항이 있나 먼저 확인하고 그것의 유효성을 검사해야하기 때문이다.
```



___

