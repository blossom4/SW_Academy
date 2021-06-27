# js_02_homework





## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다. 
  - ( F )
- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다. 
  - ( T )
- for in 문을 통해 배열의 각 요소를 순회할 수 있다. 
  - ( T )
- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false 를 반환한다. 
  - ( F )  '===' 연산자에 대한 설명이다.
- JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결과값으로 반환할 수는 없다.
  - ( F )



##  2. 다음의 Array Helper Method의 동작을 간략히 서술하시오.

- map : 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- filter : 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- find : 콜백 함수의 반환 값이 참이면 해당 요소를 반환
- every : 배열의 모든 요소가 판별 함수를 통과하면 참을 반환
- some : 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환
- reduce : 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환



## 3. 아래의 숫자 배열에 map 함수를 사용하여, 모든 아이템에 3제곱을 한 새로운 배열을 만드는 코드를 작성하시오.

```javascript
const nums = [1, 2, 3, 4]

const res = nums.map(function(num) {
    return num * num * num
})
console.log(res)
```

