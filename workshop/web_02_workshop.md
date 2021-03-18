# web_02_workshop

> **Layout 구조의 이해**
>
> **CSS Propoerty의 이해**



## 1. Semantic Tag

> **제시된 semantic.html과 semantic.css를 수정하여 다음 이미지와 같은 형태가 되도록 코드를 작성하시오.**

![제목 없음](web_02_workshop.assets/img.png)

```html
<!-- HTML -->
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="bg-lightgray mrg-4 pdd-4 b-radius">
    <h1 class="text-center">header</h1>
  </header>
  <nav class="bg-lightgray mrg-4 pdd-4 b-radius">
    <h2>nav</h2>
  </nav>
  <section class="bg-lightgray mrg-4 pdd-4 d-inline-block section-width-height b-radius">
    <h2>section</h2>
    <article class="bg-white mrg-4 pdd-4 b-radius">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class="bg-lightgray mrg-4 pdd-4 d-inline-block aside-width-height v-align-top b-radius">
    <h2>aside</h2>
  </aside>
  <footer class="bg-lightgray mrg-4 pdd-4 b-radius">
    <h2>footer</h2>
  </footer>
</body>
</html>
```

```css
/* CSS */
body {
  font-family: Arial;
  width: 800px;
}
/* 모든 스타일링 요소를 클래스로 만들어 사용합니다. */
/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */

.bg-white {
  background-color: white;
}

.bg-lightgray {
  background-color: lightgray;
}

/* 2. 모든 시멘틱 태그의 margin과 padding을 4px로 만들어주세요. */

.mrg-4 {
  margin: 4px;
}
.pdd-4 {
  padding: 4px;
}

/* 3. h1 태그를 중앙 정렬 시켜주세요. */

.text-center {
  text-align: center;
}

/* 4. section과 aside 태그의 display를 inline-block으로 바꿔주세요. */

.d-inline-block {
  display: inline-block;
}

/* 5. section 태그는 width 482px height 300px, aside 태그는 width 280px height 300px로 만들어주세요.*/

.section-width-height {
  width: 482px;
  height: 300px;
}

.aside-width-height {
  width: 280px;
  height: 300px;
}

/* 6. aside 태그에 vertical-align속성의 값을 top으로 적용해주세요.*/

.v-align-top {
  vertical-align: top;
}
/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */

.b-radius {
  border-radius: 4px;
}
```



___

