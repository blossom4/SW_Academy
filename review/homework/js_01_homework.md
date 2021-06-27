# js_01_homework





## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다. 
  - T
- EventTarget.addEventListener(type, listener)에서 listener에 작성되는 콜백 함수의 첫번째 매개변수는 발생한 이벤트를 설명하는 Event에 기반한 객체이다. 
  - T
- event.preventDefault 메서드를 통해 이벤트 동작을 취소할 수 있다. 
  - T
- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다.
  - F



## 2. DOM Event에는 다양한 종류의 Event가 존재한다.  

## 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 MDN 문서를 참고하여 간단하게 작성하시오.

- click : 포인팅 장치 버튼(모든 버튼; 주 버튼만 해당될 예정)이 엘리먼트에서 눌렸다가 놓였을 때.
- mouseover : 포인팅 장치가 리스너가 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때.
- mouseout : 포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때.
- keydown : 키가 눌렸을 때
- keyup : 키 누름이 해제될 때
- load : 리소스와 그 의존 리소스의 로딩이 끝났을 때.
- scroll : 다큐먼트 뷰나 엘리먼트가 스크롤되었을 때.
- change : The `change` event is fired for <input>, <select>, and <textarea> elements when a change to the element's value is committed by the user.
- input : 값을 받았을 때



## 3. 다음은 버튼을 클릭했을 때, 콘솔창을 통해 메시지를 확인하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.



```javascript
const button = document.__(a)__('button')

button.__(b)__(__(c)__, function () {
    console.log('Button clicked!')
})
```

(a) : createElement

(b) : addEventListenr

(c): 'click'