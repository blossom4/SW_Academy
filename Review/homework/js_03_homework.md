# js_03_homework





## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한번에 한가지 일 밖에 처리하지 못한다. 
  - (T)
- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료 되면 Call Stack에 바로 할당된다. 
  - (F) queuestack 로 먼저가서 기존의 call stack이 처리될때까지 기다린다.
- Prmoise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는 비동기 처리가 성공/실패 했을 경우 어떠한 값을 전달할지 결정한다. 
  - (T)
- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이 며, .catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다.
  - (T)



## 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- 동기함수

정해진 순서에 맞게 차례대로 진행된다.

- 비동기함수

특정 조건에서 특정하게 실행되므로 순서를 장담할 수 없다.



## 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```javascript
axios.__(a)__('https://api.example.com/data')
.__(b)__(function (response) {
    console.log(__(c)__)
})
```

(a): get

(b): then

(c): response.data



