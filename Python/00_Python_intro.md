# 00_Python_intro





# 기초 문법 (Basic Syntax)



## 주석(Comment)

- 한 줄 주석은 `#`으로 표현한다.
- 여러 줄의 주석은
  1. 한 줄씩 `#`을 사용해서 표현
  2. `"""` 또는 `'''`(multi line string)으로 표현할 수 있다. (multi line은 주로 함수/클래스를 설명하기 위해 활용된다.)

```python
# print('hi')
>>
실행되지 않는다.
```

```python
'''
THis is
multi line string
comment code.
'''
```



## 코드 라인

- python 코드는 **'1줄에 1문장(statement)'**이 원칙이다.
- 문장(statement)은 파이썬이 **실행 가능한(executable)** 최소한의 코드 단위이다.
- 기본적으로 파이썬에서는 `;`을 작성하지 않는다.
- 여러 가지 명령어를 한 줄로 표기할 때는 `;`을 작성하여 표기할 수 있다.

```python
# print
print('hi')
print('ryan')
>>
hi
ryan
```

```python
print('''hi ryan, It\'s been a long time.
nice to meet you again.''')
```



## 변수(Variable)

```python
a = 1
```

- a = 1 이다. (X)
- a에 1을 저장한다. (O)



## 할당 연산자(Assignment Operator) : `=`

- 변수는 `=`을 통해 할당(assignment) 된다.
- 해당 데이터 타입을 확인하기 위해 `type()`을 활용한다.
- 해당 값의 메모리 주소를 확인하기 위해 `id()`를 활용한다.

```python
a = 1
type(a)
>>
int
```

```python
a = 1
id(a)
>>
140729806685872
```

- 여러 가지 값을 동시에 할당할 수 있다.

```python
x, y = 1, 10
print(x, y)
>>
1 10
```

```python
# 변수 x와 y의 값을 바꾸기
x, y = 1, 10
temp = x
x = y
y = temp
print(x, y)
>>
10 1
```



## 식별자(Identifiers)

> Python에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)이다.

- 식별자의 이름은 알파벳, 밑줄(_), 숫자로 구성된다.
- 첫 글자에 숫자가 올 수 없다.
- 길이에 제한이 없다.
- 대소문자(case)를 구별한다.
- 아래의 키워드는 사용할 수 없다.

```python
import keyword
print(keyword.kwlist)
>>
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



## 데이터 타입(Data Type)

- 숫자 타입(Number Type)
- 문자 타입(String Type)
- 참/거짓 타입(Boolean Type)

## 숫자(Number) 타입

> (1) int(정수, integer)

모든 정수는 `int`로 표현된다.

8진수 : `0o`  / 2진수 : `0b`  / 16진수 : `0x`  로도 표현 가능하다.

```python
i = 1
type(i)
>>
int
```

```python
# n진수의 출력
binary_number = 0b10
octal_number = 0O10
decimal_number = 10
hexadecimal_number = 0x10
print('''
2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
''')
>>
2진수 : 2
8진수 : 8
10진수 : 10
16진수 : 16

```



> (2) float(부동소수점, 실수, floating point number)

실수는 `float`로 표현된다.

그러나 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값이 되지 않는다.

```python
i = 3.14
type(i)
>>
float
```

컴퓨터식 지수 표현 방식

- e를 사용할 수 있다.

```python
pi = 3.14e-2
print(pi, type(pi))
>>
3.14 <class 'float'>
```

실수의 연산

- 실수의 경우 실제로 값을 처리하기 위해서는 조심해야한다.

```python
# 실수의 뺄셈
3.5 - 3.12
>>
0.3799999999999999
```

```python
# round() 는 0~4는 내림
# 짝수에서는 5는 내림 / 홀수 에서는 5는 올림
round(3.5 - 3.12)
>>
0.38
```

```python
0.38 == 3.5 - 3.12
>>
False
```

```python
# math 모듈 활용
import math
a = 0.38
b = 3.5 - 3.12
math.isclose(a, b)
>>
True
```



> (3) complex(복소수, complex number)

각각 실수로 표현되는 실수부와 허수부를 가진다.

복소수는 허수부를 `j`로 표현한다.

```python
a = 3 - 4j
type(a)
>>
complex
```

```python
# 복소수 문자열을 변환할 때, 가운데 + 혹은 - 연산자 주위에 공백을 포함하면 안된다.
complex('1+2j')
>>
(1+2j)
```



## 문자(String) 타입

> 기본 활용법

- 문자열은 Single quotes(`'`)나 Double quotes(`"`)를 활용하여 표현 가능하다.
- 둘 중 **한 가지 방법**을 유지하여 사용하는 것이 좋다.

```python
name = 'hi'
name2 = 1
print(name, type(name))
print(name2, type(name2))
>>
hi <class 'str'>
1 <class 'int'>
```

```python
# 사용자에게 받은 입력은 기본적으로 str이다.
name = input()
print(name, type(name()))
>>
1
1 <class 'str'>
```

```python
# 문자열은 변수화 / + 연산자로 이어붙이기 / * 연산자로 반복시키기 모두 가능하다.
a = 'hi'
b = 'ryan'
a * 3 + b
>>
hihihiryan
```



> 이스케이프 시퀀스

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 사용하여 구분한다.

예약문자 / 의미

- `\n`	>	줄 바꿈
- `\t`    >    탭
- `\0`    >    널(Null)
- `\r`    >    줄 맨앞으로 (Carriage return)



> 문자열 보간법(String interpolation)

- `%-formating`
  - `%d` : 정수
  - `%f` : 실수
  - `%s` : 문자열
- `str.format()`
- `f-string` : python 3.6 이후 버전에서만 지원

```python
# %-formating
name = 'ryan'
grade = 3.5
print('hi, %s' % name)
print('my grade is %d' % grade)
print('my grade is %f' % grade)
>>
hi, ryan
my grade is 3
my grade is 3.500000
```

```python
# str.format()
name = 'ryan'
print('hi, {}'.foramt(name))
>>
hi, ryan
```

```python
# f-string
name = 'ryan'
print(f'hi, {name}')
>>
hi, ryan
```

---

```python
# datetime 모듈
import datetime
today = datetime.datetime.now()
print(today)
>>
2021-01-18 21:12:07.668363
```

```python
# f-string
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}이다.')
>>
오늘은 21년 01월 18일 Monday이다.
```



## 참/거짓(Boolean) 타입

- python에는 `True`와 `False`로 이뤄진 `bool`타입이 있다.

- 비교 / 논리 연산을 수행할 때 활용된다.

- 다음은 `False`로 변환된다.

```python
0, 0.0, (), [], {}, '', None
```

```python
# True 와 False의 타입
print(type(True))
print(type(False))
>>
<class 'bool'>
<class 'bool'>
```



> None 타입

python에서는 값이 없음을 표현하기 위해 None 타입이 존재한다.

```python
print(type(None))
>>
<class 'Nonetype'>
```

```python
# None을 표현할 때 대소문자를 지켜야한다.
a = None
print(a)
>>
None
```



## 형변환(Type conversion, Typecasting)

> 암시적 형변환(Implicit Type Conversion)

사용자가 의도하지 않았지만, python 내부적으로 자동 형변환 하는 경우이다.

- `bool`
- Numbers (`int`, `float`, `complex`)

```python
# boolean과 integer의 연산
True + 2
>>
3
```

```python
# int, float, complex의 연산
int_number = 3
float_number = 5.0
res = int_number + float_number
print(res, type(res))
>>
8.0 <clss 'float'>
```



> 명시적 형변환(Explicit Type Conversion)

위의 경우를 제외하고는 모두 명시적으로 형변환을 해주어야한다.

- string > integer : 형식에 맞는 숫자만 가능
- integer > string : 모두 가능

```python
# int > str
str(1) + '등'
>>
'1등'
```

```python
# str > int
a = '3'
print(int(a), type(int(a)))
>>
3 <class 'int'>
```



## 연산자(Operator)

- 산술 연산자(Arithmetic operator)
- 비교 연산자(Comparing operator)
- 논리 연산자(Logical operator)
- 복합 연산자
- 기타 연산자



> 산술 연산자(Arithmetic operator)

연산자	/	내용

- `+`	>	덧셈
- `-`    >    뺄셈
- `*`    >    곱셈
- `/`    >    나눗셈
- `//`  >    몫
- `%`    >    나머지(modulo)	
- `**`  >    거듭제곱

나눗셈 (`/`) 은 항상 float를 돌려준다.

```python
# divmod 함수
quotient, remainder = divmod(5, 2)
print('몫은 {}, 나머지는 {}'.format(quotient, remainder))
>>
몫은 2, 나머지는 1
```



> 비교 연산자(Comparing operator)

연산자	/	내용

- `<`    >    미만
- `<=`  >    이하
- `>`    >    초과
- `>=`  >    이상
- `==`  >    같음
- `!=`  >    같지않음
- `is`  >    객체 아이덴티티
- `is not` > 부정 객체 아이텐티티



> 논리 연산자(Logical operator)

연산자	/	내용

- `a and b`   >    a와 b 모두 True여야 True
- `a or b`     >    a와 b 모두 False여야 False
- `not a`       >    True면 False, False면 True

```python
# not
print(not True)
print(not 0)
>>
False
True
```



> 단축평가(Short-circuit evaluation)

- 첫 번째 값이 확실할 때, 다음 값은 확인 하지 않음
- 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

```python
'a' and 'b'
>>
b
```

```python
'a' or 'b'
>>
a
```

```python
# and short-circuit evaluation
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)
>>
5
0
0
0
```

```python
# or short-circuit evalution
print(3 or 5)
print(3 or 0)
print(0 or 3)
print(0 or 0)
>>
3
3
3
0
```



> 복합 연산자

연산자	/	내용

- `a += b`    >    a = a + b
- `a -= b`    >    a = a - b
- `a *= b`    >    a = a * b
- `a /= b `    >    a = a / b
- `a // b`    >    a = a // b
- `a % b`      >    a = a % b
- `a ** b`    >    a = a ** b

```python
# +=
cnt = 0
while cnt < 5:
    print(cnt, end='')
    cnt += 1
>>
01234
```



> 기타 연산자

연결(Concatenation)

- 숫자가 아닌 자료형은 `+` 연산자로 합칠 수 있다.

```python
# string
'abc' + 'def'
>>
'abcdef'
```

```python
# list
[1, 2, 3] + [4, 5, 6]
>>
[1, 2, 3, 4, 5, 6]
```



포함(Containment test)

- `in` 연산자를 사용해서 요소가 속해있는지 여부를 확인할 수 있다.

```python
# string
'y' in 'hi, ryan'
>>
True
```

```python
# list
list_a = [1, 2, 3]
3 in a
>>
True
```

```python
# range
50 in range(50)
>>
False
```



식별(Identity)

- `is` 연산자를 통해 동일한 object인지 확인할 수 있다.

```python
# 같은 list지만, 다른 object이다.
a = []
b = []
print(a == b, a is b)
print(id(a), id(b))
>>
True False
1343179433216 1343179429376
```

```python
# -5 ~ 256 이라는 특정 범위의 숫자는 id가 같게 설정했다.
a = 1
b = 1
print(a is b)
print(id(a), id(b))
>>
True
140729805637296 140729805637296
```

```python
# 공백없는 알파벳 문자열의 id는 같게 설정했다.
a = 'ryan'
b = 'ryan'
a is b
>>
True
```

```python
# 공백없는 알파벳 문자열이나 특정 범위의 숫자 이외에는 id값이 원래 다르다.
a = 'ryan!'
b = 'ryan!'
a is b
>>
False
```



Indexing / Slicing

`[]`를 통해 값에 접근하고, `[:]`을 통해 리스트를 슬라이싱할 수 있다.

```python
# indexing
a = 'hi, ryan'
a[3]
>>
' '
```

```python
# slicing
a = 'hi, ryan'
a[2:5]
>>
', r'
```



## 연산자 우선순위

0. `()`로 grouping
1. Slicing
2. Indexing
3. `**` 제곱연산자
4. `+`, `- `(양수, 음수 부호) 단항연산자
5. `*`, `/`, `%` 산술연산자
6. `+`, `-` 산술연산자
7. `in`, `is` 비교연산자
8. `not`
9. `and`
10. `or`

> 가장 좋은 방법은 **`()`으로 grouping을 확실하게** 하는 것이다.





## 표현식(Expression)

> 표현식 > evaluate > 값

- 하나의 값(value)으로 환원(reduce)될 수 있는 문장
- 식별자(identity), 값(literal), 연산자(operator)로 구성된다.



## 문장(Statement)

- python이 실행 가능한 최소한의 코드 단위 (a syntactic unit of programming)

```python
# value - executable
'ryan'
>>
ryan
```

```python
# expression - executable
5 * 21 - 4
>>
101
```

