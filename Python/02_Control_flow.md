# 02_Control_flow



## 제어문(Control Statement)

코드실행의 순차적인 흐름을 제어 (Control Flow)

- 조건문(Conditional statement)
- 반복문(Iteration statement)



## 조건문(Conditional Statement)

`if` 문은 반드시 **참 / 거짓을 판단할 수 있는 조건**과 함께 사용이 되어야 한다.



> if 조건문의 구성

활용법

- 문법

  ```python
  if <expression1>:
      <code block>
  elif <expression2>:
      <code block>
  else:
      <code block>
  ```

- `expression`에는 일반적으로 참 / 거짓에 대한 조건식이 들어간다.
- 조건이 **참**인 경우 `:` 이후의 명령을 수행한다.
- 조건이 **거짓**인 경우 : `elif` 혹은 `else` 이후의 명령을 수행한다.
- `elif`는 여러 개가 있을 수 있고, `elif`, `else` 모두 선택적이다.

> 주의사항

- **들여쓰기**를 유의하여야 한다.
- python에서는 code block을 Java나 C의 `{}`와 달리 **들여쓰기**로 판단하기 때문이다.
- **4spaces** / **Tab**

```python
# 조건문을 통해 변수 num의 값과 홀/짝 여부를 출력
num = int(input('숫자를 입력하세요 : '))
if num % 2:
    print('홀수입니다.')
else:
    print('짝수입니다.')
>>
숫자를 입력하세요 : 2
짝수입니다.
```



> elif 복수 조건

2개 이상의 조건을 활용할 경우 `elif <condition>:`을 활용한다.

```python
# 변수 score에 따른 평점을 출력
score = int(input('점수를 입력하세요 : '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
>>
점수를 입력하세요 : 3
F
```



> 중첩 조건문(Nested Conditional Statement)

조건문은 다른 조건문에 중첩할 수 있다.

```python
score = int(input('점수를 입력하세요 : '))

if score >= 90:
    print('A')
    if score >= 95:
        print('참 잘했어요:)')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
>>
점수를 입력하세요 : 96
A
참 잘했어요:)
```



> 조건 표현식(Conditional Expression)

- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 사용한다.

- **삼항 연산자(Ternary Operator)** 라고 부르기도 한다.

  ```python
  true_value if <condition> else false_value
  ```



## 반복문(Iteration Statement)

- `while`
- `for`



> while 반복문

`while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.



활용법

- 문법

  ```python
  while <condition>:
      <code block>
  ```

주의사항

- `while`문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요하며, 이후 실행될 code block은 **4space**로 **들여쓰기**를 한다.
- 반드시 **종료조건**을 설정해야한다.

```python
# while문 '안녕'이라고 입력할 때까지 인사하는 코드
user_input = ''
while user_input != '안녕':
    user_input = input('인사해줘 : ')
>>
인사해줘 : 반가워
인사해줘 : 하이
인사해줘 : 누구니
인사해줘 : 안녕
```

```python
# 합(Summation)
# input()은 기본적으로 string으로 받는다.
num = int(input())
i = 1
res = 0
while i <= num:
    res += i
    i += 1
print(res)
>>
10
55
```

```python
# 한자리씩 출력
num = int(input())
while num > 0:
    print(num % 10)
    num = num // 10
>>
185
5
8
1
```



> for문

`for` 문은 sequence(string, tuple, list, range)나 다른 순회가능한 객체(iterable)의 요소들을 순회한다.



활용법

- 문법

  ```python
  for <temporary variable> in <iterable data>:
      <code block>
  ```

- for 문과 if문 활용

```python
# print only odd number range in 1 ~ 10
for i in range(10):
    if i % 2:
        print(i)
>>
1
3
5
7
9
```



> enumerate()

인덱스(index)와 값(value)을 함께 활용 가능하다.

- `enumerate(iterable, start = 0)`

```python
# enumerate()를 활용해서 출력
# enumerate(iterable, start = 0)
lunch = ['짜장면', '초밥', '피자', '햄버거']
for l in enumerate(lunch):
    print(l, type(l))
>>>>
(0, '짜장면') <class 'tuple'>
(1, '초밥') <class 'tuple'>
(2, '피자') <class 'tuple'>
(3, '햄버거') <class 'tuple'>
```

```python
# tuple의 요소를 따로 출력할 수 있다.
lunch = ['짜장면', '초밥', '피자', '햄버거']
for index, menu in enumerate(lunch):
    print(index)
    print(menu)
>>
0
짜장면
1
초밥
2
피자
3
햄버거
```



## 반복제어(`break`, `continue`, `for - else`)

> break

반복문을 종료한다.

- `for`, `while` 문에서 빠져나간다.

```python
# while문에서 break의 활용
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
>>
0
1
2
```

```python
# for문에서 break 활용
for i in range(10):
    if i > 5:
        print('5보다 커졌습니다.')
        break
    print(i)
```



> continue

`continue`문은 continue 이후의 코드를 수행하지 않고 다음 요소부터 반복을 수행한다.

```python
# range 내에서 짝수만 출력
for i in range(6):
    if i % 2:
        continue
    print(i)
>>
0
2
4
```

```python
# more than 20-year old?
ages = [10, 23, 8, 30, 25, 31]
for i in ages:
    if i < 20:
        continue
    else:
        print(i, 'adult')
>>
23 adult
30 adult
25 adult
31 adult
```



> else

끝까지 반복문을 실행한 이후에 실행된다.

- 반복에서 리스트의 소진이나(`for`) 조건이 거짓이 되어서(`while`) 종료할 때 실행된다.
- 하지만 반복문이 `break`으로 종료될 때는 실행되지 않는다.

```python
# break / for - else
for i in range(3):
    print(i)
    if i == 3:
        print('break')
        break
else:
    print('else')
>>
0
1
2
else
```



> pass

아무것도 하지 않는다.

- 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용한다.

```python
# continue
for i in range(5):
    if i == 2:
        continue
    print(i)
>>
0
1
3
4
```

```python
# pass
for i in range(5):
    if i == 3:
        pass
    print(i)
>>
0
1
2
3
4
```

