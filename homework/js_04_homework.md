# js_04_homework





## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하 는 역할을 한다. 
  - (T)
- XMLHttpRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드 로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다. 
  - (T)
- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.
  - (T)



## 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```javascript
console.log('Hello SSAFY!')

setTimeout(function () {
    console.log('I am from setTimeout')
}, 1000)

console.log('Bye SSAFY!')
```

1. 'Hello SSAFY!' -> Call Stack -> 처리
2. 'I am from setTimeout' -> Web API -> 최소1000ms 걸려서 Task Queue로 들어간다.
3. 'Bye SSAFY!'는 기다려주지 않고 바로 Call Stack으로 들어가서 처리된다.
4. Call Stack이 비면 Task Queue에 있던 'I am from setTimeout'이 Call Stack으로 들어가 처리된다.



## 3.  JS는 Event loop를 기반으로 하는 Concurrency model을 가지고 있다고 한다.  

## Concurrency 키워드의 특징을 작성하고, 이와 비슷한 키워드로 비교되는 Parallelism의 개념과 두 개념의 차이점을 서술 하시오.

- Concurrency

  프로그램을 실행할 때 단 하나의 실행 순서를 갖도록 하는 제약을 없애고 각 부프로그램이 다른 부프로그램과 병렬적으로 동시에 실행되는 것.

- Parallelism

  컴퓨터 시스템의 여러 부분의 동시 작동을 말하며, 여러 프로그램의 동시 처리또는 여러 컴퓨터 시스템의 동시 작동을 뜻한다.

- 차이점

  단일로 실행되지만 그안에서 여러가지 동작이 동시에 수행된다는 점과 애초에 여러가지 부분에서 여러가지가 동시에 수행되는것은 다르다.