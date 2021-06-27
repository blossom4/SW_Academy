# README



- 기본 세팅
  - 가상화
  - migrate
  - pip install Faker
  - shell_plus (example data 받아옴)
  - loaddata (dumpdata 받아옴)





- like 구현

  

index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Community</h1>
  {% if user.is_authenticated %}
    <a href="{% url 'community:create' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
  <hr>
  {% for review in reviews %}
    <p><b>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></b></p>
    <p>글 번호: {{ review.pk }}</p>
    <p>글 제목: {{ review.title }}</p>
    <p>글 내용: {{ review.content }}</p>
    <form class="d-inline like-form" data-review-id="{{ review.pk }}">
      {% csrf_token %}
      {% if user in review.like_users.all %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color: crimson" data-heart-id="{{ review.pk }}"></i>
        </button>
      {% else %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg not-liked" style="color: black"  data-heart-id="{{ review.pk }}"></i>
        </button>
      {% endif %}
    </form>
  <span data-likecount-id="{{ review.pk }}">{{ review.like_users.all|length }}</span> 명이 이 글을 좋아합니다.<br>
    <a href="{% url 'community:detail' review.pk %}">[detail]</a>
    <hr>
  {% endfor %}

  <script>
    const likeForms = document.querySelectorAll('.like-form')
    const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value
    likeForms.forEach((form) => {
      form.addEventListener('submit', (e) => {
        e.preventDefault()
        const requestData = {
          url: `http://127.0.0.1:8000/community/reviews/${form.dataset.reviewId}/like/`,
          method: 'post',
          headers: {
            'X-CSRFToken': csrfToken,
          },
        }
        axios(requestData)
          .then((res) => {
            const { liked, likeCount } = res.data
            const heart = document.querySelector(`[data-heart-id="${form.dataset.reviewId}"]`)
            if (liked) {
              heart.style = "color: crimson"
            } else {
              heart.style = 'color: black'
            }
            const likeCountSpan = document.querySelector(`[data-likecount-id="${form.dataset.reviewId}"]`)
            likeCountSpan.innerText = likeCount
          })
          .catch((err) => {
            console.log(err)
          })
      })
    })
  </script>
{% endblock %}
```



views.py

```python
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        data = {
            'liked': liked,
            'likeCount': review.like_users.count(),
        }
        return JsonResponse(data)
    return redirect('accounts:login')
```



- follow 구현

```html
<div class="jumbotron text-center text-white bg-dark">
  <p class="lead mb-1">작성자 정보</p>
  <h1 class="display-4">{{ person.username }}</h1>
  <hr>
  {% with followings=person.followings.all followers=person.followers.all %}
    <p class="lead">
      팔로잉 : {{ followings|length }} / 팔로워 : <span id="followerCount">{{ followers|length }}</span>
    </p>
    <!-- 팔로우 버튼 -->
    {% if request.user != person %}
      <form id="follow-form">
        {% csrf_token %}
        {% if request.user in followers %}
          <button id="followBtn" class="btn-secondary btn-lg" role="button">Unfollow</button>
        {% else %}
          <button id="followBtn" class="btn-primary btn-lg" role="button">Follow</button>
        {% endif %}
      </form>
    {% endif %}
  {% endwith %}
</div>
<script>
  const followForm = document.querySelector('#follow-form')
  const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value 
  followForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const requestData = {
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/follow/{{ person.pk }}/`,
      headers: {'X-CSRFToken': csrfToken},
    }

    axios(requestData)
      .then((res)=>{
        const { following, followerCount } = res.data
        const followBtn = document.querySelector('#followBtn')
        const followerCountSpan = document.querySelector('#followerCount')

        if (following) {
          followBtn.innerText = 'Unfollow'
          followBtn.classList.toggle('btn-primary')
          followBtn.classList.toggle('btn-secondary')

        } else {
          followBtn.innerText = 'Follow'
          followBtn.classList.toggle('btn-secondary')
          followBtn.classList.toggle('btn-primary')
        }
        followerCountSpan.innerText = followerCount
      })
      .catch((err)=>{
        console.log(err)
      })
  })
</script>
```



views.py

```python
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                following = False
            else:
                person.followers.add(user)
                following = True
            data = {
                'following': following,
                'followerCount': person.followers.count() 
            }
            return JsonResponse(data)
    return redirect('accounts:profile', person.username)
```



- infinite scroll 구현



```html
{% extends 'base.html' %}

{% block content %}
  <h1>Movies</h1>
  <!-- {% for movie in movies %}
    <h3>{{ movie.title }}</h3>
    <p>
      {% for genre in movie.genres.all %}
        <span>{{ genre.name }}</span>
      {% endfor %}
    </p>
    {% if movie.overview %}
      <p>{{ movie.overview|truncatechars:60 }}</p>
    {% else %}
      <p>줄거리 없음</p>
    {% endif %}
    <a href="{% url 'movies:detail' movie.pk %}">[detail]</a>
    <hr>
  {% endfor %} -->

    <div id="movie_list">
      <div v-for="movie in movies" class="my-5 border border-2 border-primary rounded p-2">
        <h3 v-text="movie.fields.title" class="m-1"></h3>
        <hr class="text-primary">
        <p v-if="movie.fields.overview" v-text="movie.fields.overview" class="m-1"></p>
        <p v-else>줄거리 없음.</p>
      </div>

    </div>
  
    <script>
      const movie_list = new Vue({
        el: '#movie_list',
        data: {
          pageNum: 1,
          url: 'http://127.0.0.1:8000/movies/',
          movies: [],
        },
        methods: {
         getMovies() {
           const requestData = {
             method: 'get',
             url: `${this.url}?page=${this.pageNum}`,
             headers: {'X-Requested-With': 'XMLHttpRequest'},
           }
           axios(requestData)
            .then((res)=>{
              this.movies.push(...res.data)
              this.pageNum += 1
            })
            .catch((err)=>{
              console.log(err)
            })
         },
         scrollEnd() {
           const { scrollHeight, scrollTop, clientHeight } = document.documentElement
            // console.log( scrollHeight, scrollTop, clientHeight )
           
           if (scrollHeight - scrollTop - 1 < clientHeight) {
            this.getMovies()

           }
         }
        },
        created() {
          this.getMovies()
          document.addEventListener('scroll', this.scrollEnd)
        }  
        
      })
    </script>
{% endblock %}
```



views.py

```python
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    pageNum = request.GET.get('page')
    movies = paginator.get_page(pageNum)

    if request.is_ajax():
        data = serializers.serialize('json', movies)
        return HttpResponse(data, content_type='application/json')
    else:
        return render(request, 'movies/index.html')
```

