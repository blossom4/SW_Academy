# 03_Function1



## 함수(function)

특정한 기능(function)을 하는 코드의 묶음



> 함수를 쓰는 이유

- 높은 가독성
- 재사용성
- 유지보수 / 코드의 기능별 분화



> 함수의 선언과 호출

- 함수 선언은 `def`로 시작하여 `:`로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만든다.
- 함수는 매개변수(parameter)를 넘겨줄 수도 있다.
- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도있다.
  - `return`값이 없으면 `None`을 반환한다.
- 함수는 호출을 `function_name() / function_name(value1, value2)` 와 같이 한다.



> 활용법

```python
def <function name>(parameter):
    <code block>
    return value
```



> 예시

```python
# define function
def my_sum(a, b):
    return a + b

res = my_sum(1, 2)
print(res)
>>
3
```

```python
# function print() is NoneType.
print_type = print('a')
print(type(print_type))
>>
a
<class 'NoneType'>
```



## 함수의 Output

> 함수의 return

- 함수는 반환되는 값이 있으며, 이는 어떠한 것이라도 상관없다.

- 단, **오직 한 개의 객체**만 반환된다.
- 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

```python
# 아무것도 return하지 않으면 자동으로 None을 반환한다.
def hi(name):
    print(f'hi, {name}')
a = hi('ryan')
print(a, type(a))
>>
hi, ryan
None <class 'NoneType'>
```

```python
# 여러개의 값을 반환하려고하면 튜플로 묶어서 하나로 반환한다.
def my_name(name):
    return 'hi', name
a = my_name('ryan')
print(a, type(a))
>>
('hi', 'ryan') <class 'tuple'>
```



## 함수의 입력(Input)

> 매개변수(parameter) & 인자(argument)

1. 매개변수(parameter)

   ```python
   def func(x):
       return x + 2
   ```

   - x는 매개변수(parameter)이다.
   - 입력을 받아 함수 내부에서 활용할 **변수**이다.
   - **함수의 정의** 부분에서 볼 수 있다.

2. 전달인자(argument)

   ```python
   func(2)
   ```

   - 2는 전달인자(argumnet)
   - 실제로 전달되는 입력값이다.
   - **함수를 호출**하는 부분에서 볼 수 있다.



## 함수의 인자

함수는 입력값(input)으로 인자(argument)를 넘겨줄 수 있다.



> 위치 인자(Positional arguments)

함수는 기본적으로 인자를 위치로 판단한다.

```python
# 원기둥의 반지름(r)과 높이(h)를 받아서 부피를 return하는 함수
# 입력값의 위치에 따라 인자가 다르다.
def cylinder(r, h):
    return 3.14 * (r ** 2) * h
print(cylinder(2, 5))
print(cylinder(5, 2))
>>
62.800000000000004
157.0
```



> 기본 인자 값(Default argument values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있다.

- 활용법

  ```python
  def func(parameter1 = value1):
      return parameter1
  ```

  

> 예시

```python
# = ''기본 인자 값 설정
def greeting(name = 'anonymous'):
    print(f'hi, {name}')
greeting()
>>
hi, anonymous
```

```python
# 기본 인자 값이 있는 것 '뒤에' 없는 것을 같이 쓸 수 없다.
# 기본 인자 값이 있는 것이 뒤로 가야한다.
def greeting(age, name = 'anonymous'):
    print(f'hi, I\'m {name}. {age} year old.')
    
greeting(29)
greeting(29, 'ryan')
>>
hi, I'm anonymous. 29 year old.
hi, I'm ryan. 29 year old.
```



> 키워드 인자(Keyword arguments)

키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

- **단, 키워드 인자를 활용한 다음에 위치 인자를 다시 활용할 수없다.**

```python
# 키워드를 모두 제시하면 순서가 바뀌어도 된다.
def greeting(age, name = 'anonymous'):
    print(f'hi, I\'m {name}. {age} year old.')
    
greeting(name = 'ryan', age = 29)
>>
hi, I'm ryan. 29 year old.
```



> 가변 인자 리스트(Arbitrary argument lists)

- 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트 *args를 활용한다.

- 가변 인자 리스트는 tuple 형태로 처리가 되고, 매개변수에 `*`로 표현한다.

활용법

```python
def func(a, b, *args):
```

- *args : 임의의 개수의 위치인자를 받는다.
- 대부분, 가변 인자 리스트는 매개변수 목록의 마지막에 온다.

```python
# *args가 앞에 올 경우 어디까지가 학생이고 교수인지 구분 못하기 때문에 에러발생
# 가변인자가 뒤에 있으면 문제가 없다. (앞에 prof가 확실하므로)
def students(prof, *args):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')

students('youcho', 'ryan', 'max')
>>
ryan
max
존경하는 교수님 youcho
```



> 가변 키워드 인자(Arbitrary keyword arguments)

- 정해지지 않은 키워드 인자들은 `dict`형태로 처리가 되며, `**`로 표현한다.

- 보통 `kwargs`이름을 사용하고, `**kwargs`를 통해 인자를 받아 처리할 수 있다.

활용법

```python
# 임의의 개수의 키워드 인자를 받음
def func(**kwargs):
```

```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    print(kwargs.items())
    for name, value in kwargs.items():
        url += f'{name}={value}&'
    return url
my_url(sidoname='서울', key='asdf')
>>
dict_items([('sidoname', '서울'), ('key', 'asdf')])
'https://api.go.kr?sidoname=서울&key=asdf&'
```

