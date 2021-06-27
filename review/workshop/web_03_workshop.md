# web_03_workshop

> **Bootstrap의 이해**
>
> **Bootstrap Component 활용**

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
  <!-- 1. Nav -->
  <!--d-flex 세로정렬이 기본인데 가로정렬로 해당축을 바꾸어준다. justify는 메인축 align은 반대축-->
  <nav class="fixed-top d-flex justify-content-between align-items-center bg-dark">
    <a href="#" class="ms-5">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <!--메인축을 가로로바꿔주고 양끝으로 보낸다. list-line은 앞의 불릿바크를 없애주고 m-0은 중앙정렬이 안맞는것같을때 마진을 아예 없애준다.-->
    <ul class="d-flex justify-content-between list-inline m-0">
      <!--mx-3 마진은 주변과의 간격 padding은 내부의 간격-->
      <li class="mx-3"><a href="#" class="text-white text-decoration-none">Home</a></li>
      <li class="mx-3"><a href="#" class="text-white text-decortion-none">Community</a></li>
      <li class="ms-3 me-5"><a href="#" class="text-white text-decoration-none">Login</a></li>
    </ul>
  </nav>

  <!-- 2. Header -->
  <header class="d-flex flex-column justify-content-center align-items-center">
      <div class="display-1 text-white fw-bold">Cinema</div>
      <div class="display-1 text-white">Community</div>
      <a href="#" class="btn btn-primary my-3">Let's Go</a>
  </header>

  <!-- 3. Section -->
  <section>
    <h2 class="text-center">Used Skills</h2>
    <article class="d-flex justify-content-center mx-5">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p class="text-center">Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p  class="text-center">HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p  class="text-center">CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="d-flex justify-content-center align-items-center bg-primary fixed-bottom">
    <p class="m-0 text-white">HTML & CSS project. Created by Young-shin Jo</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>
```



___

