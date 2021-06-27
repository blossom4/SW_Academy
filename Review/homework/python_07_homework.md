# python_07_homework



## 1. Type Class

> **Python은 객체 지향 프로그래밍 언어이다. **
>
> **Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.**

```python
print(type(1))
print(type(1+j))
print(type('1'))
print(type[1])
print(type(map(int, ['1'])))
>>
<class 'int'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'map'>
```



___

## 2. Magic Method

> **아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.**

- `__init__`

  클래스 생성자이다. 클래스가 인스턴스를 생성할 때에 호출되는 특별한 method이다.

  init 앞뒤에 붙은 __(underscore)은 python이 자동으로 호출하는 method를 명시한 것이다.

- `__del__`

  클래스 소멸자이다. python 클래스의 인스턴스가 소멸될 때 호출된다. 

- `__str__`

  str() 생성자에 의해 호출되며 print() 함수에 의해 암묵적으로 사용된다.

  사용자에게 보여주기 적당한 형태의 문자열을 반환한다.

- `__repr__`

  이 method가 반환한 문자열은 명확해야하며, 가능하면 표현된 객채를 재생성하는 데 필요한

  소스코드와 일치해야한다.



___

## 3. Instance Method

> **.sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. **
>
> **이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.**

```python
# .sort()
a = [3, 2, 1]
a.sort()
print(a)
>>
[1, 2, 3]
```

```python
# .upper()
a = 'a'
print(a.upper())
>>
A
```

```python
# .sample()
import random
a = random.sample(range(5), 2)
print(a)
>>
[2, 4]
```

```python
# .pop()
a = [1, 2, 3]
print(a.pop(0))
>>
1
```



## 4. Module Import

> **위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, **
>
> **아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 완성하시오.**

```python
# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)
```

```python
# (a) = 파일명 (b) = 함수명 (c) = user가 원하는 이름
from fibo import fibo_recursion as recursion

recurtion(4)
```



___

