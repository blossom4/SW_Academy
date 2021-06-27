# js_04_workshop



```html
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      <!-- <form action="{% url 'articles:likes' article.pk %}" method="POST"> -->
        <form class="like-form" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button id="like-{{ article.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-{{ article.pk }}">좋아요</button>
        {% endif %}
      </form>
    </div>
    <p><span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span>명이 이 글을 좋아합니다.</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}

  <!-- AXIOS -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

  <script>
    const forms = document.querySelectorAll('.like-form')
    // console.log(forms)
    // data의 구조를 파악하고, 내용이 어떠한 이름으로 저장되어있는지 잘 확인해서 뽑아와야한다.
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // console.log(csrftoken)
    forms.forEach(function (form) {
      // console.log(form)
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        // console.log(event.target.dataset)
        const articleId = event.target.dataset.articleId
        const URL = `http://127.0.0.1:8000/articles/${articleId}/likes/`

        const requestData = {
          method: 'post',
          url: URL,
          headers: {'X-CSRFToken': csrftoken}
        }

        axios(requestData)
          .then(function(response) {
            console.log(response.data) // True or False
            const liked = response.data.liked

            const likeBtn = document.querySelector(`#like-${articleId}`)
            const likeCount = document.querySelector(`#like-count-${articleId}`)

            likeCount.innerText = response.data.likedCount

            if (liked){
              // 좋아요가 눌림
              likeBtn.innerText = '좋아요 취소'
            }
            else {
              likeBtn.innerText = '좋아요'
            }
          })
          .catch(function(error) {
            console.log(error)
          })
      })
    })
  </script>
{% endblock %}

```



___



```python
from django.http.response import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
            liked = False
        else:
            # 좋아요 누름
            article.like_users.add(request.user)
            liked =True
        
        like_status = {
            'liked': liked,
            'likedCount': article.like_users.count(),
        }
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')
```

