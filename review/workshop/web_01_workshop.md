# web_01_workshop

> HTML tag
>
> CSS Selector



## 1. img tag

> **아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는 ![img]() tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.**

```html
<img src='../image/my_photo.png'> 
```





___

## 2. 파일경로

>  **위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. **
>
> **이를 해결 하려면 이미지 경로를 __(b)__ 로 바꾸어 작성하면 된다.**
>
> **__(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오**

(a) 절대경로

(b) 상대경로



___

## 3. Hyper Link

> **출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.**

```html
<a href='www.ssafy.com'>
  <img src='../image/my_photo.png'>
</a>
```



___

## 4. 선택자

> **아래의 코드를 작성하고 결과를 확인 하시오**

```html
<div id="ssafy">
    
    <h2>어떻게 선택 될까?</h2>
    <p>첫 번째 단락</p>
    <p>두 번째 단락</p>
    <p>세 번째 단락</p>
    <p>네 번째 단락</p>
</div>
```

```html
<!-- 자식들 중에 2번째가 p태그라면 red로 바꾼다. -->
#ssafy > p:nth-child(2) {
	color: red;
}
>>
첫 번째 단락이 red가 된다.
```

![](web_01_workshop.assets/workshop4-1.png)

```html
<!-- p타입인 자식들 중에 2번째를 blue로 바꾼다. -->
#ssafy > p:nth-of-type(2) {
	color: blue;
}
두 번째 단락이 blue가 된다.
```

![](web_01_workshop.assets/workshop4-2.png)

```html
<!-- 자식들 중에 2번째가 p태그라면 red로 바꾼다. -->
<!-- p타입인 자식들 중에 2번째를 blue로 바꾼다. -->
```

