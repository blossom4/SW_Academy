# django_06_workshop



## Media file with HTML input

```html
<form action="#" method="POST" enctype="___(a)___">
  <label for="data">UPLOAD: </label>
  <input type="file" name="data" id="data" accept="___(b)___">
  <input type="submit" value="submit"
</form>
```



1. 태그를 사용할 경우 반드시 사용해야 하는 enctype 속성 값 (a)를 작성하시오.

```html
(a): multipart/form-data
```

​	2. accept 속성은 파일 업로드 제어에서 선택할 수 있는 파일 유형을 정의하는 속성이 며 input 태그의 type이 file일 경우에만 유효하다. 예를 들어 표준 비디오 형식 뿐만 아니라 PDF 파일도 받을 수 있어야 할 때, 빈칸 (b)에 들어갈 알맞은 속성 값을 작성하시오.

```html
(b): video/*|image/*
```

