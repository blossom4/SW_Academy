# 04_Function2



## Function / scope

함수는 코드 내부에 공간(scope)를 생성한다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분된다.

- 전역 스코프(`global scope`) : 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

```python
# global variable a
a = 10

def func(b):
    c = 20
    print(a)
    # parameter b
    print(b)
    # local variable c
    print(c)
func(5)
>>
10
5
20
```



## 이름 검색(resolution) 규칙

python에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있다.

이것을, `LEGB rule` 이라고 부르고, 다음 순서로 찾아나간다.

- `L`ocal scope : 정의된 함수
- `E`nclosed scope : 상위 함수
- `G`lobal scope : 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope : python안에 내장되어 있는 함수 또는 속성



## 재귀 함수(Recursive function)

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻한다.

알고리즘을 설계 및 구현에서 유용하게 활용된다.



> 팩토리얼 계산

```python
# recursive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(3))
>>
6
```

> 피보나치 수열

```python
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n -2)
fib(5)
>>
8
```

