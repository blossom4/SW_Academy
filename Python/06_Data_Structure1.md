# 06_Data_Structure1

데이터 구조(Data Structure)란 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법을 말한다.



> **Program = Data Structure + Algorithm**

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조
  - 문자열(String)
  - 리스트(List)
- 데이터 구조에 적용 가능한 Built-in Function



##  문자열(String)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)
>
> 문자열의 다양한 조작법(method)
>
> https://docs.python.org/ko/3/library/stdtypes.html#string-methods



## 조회 / 탐색

> **.find()**

첫 번째 위치를 반환한다. 없으면 -1을 반환한다.

```python
a = 'apple'
a.find('a')
>>
0
```



> **.index()**

첫 번째 위치를 반환한다. 없으면, 오류가 발생한다.

```python
a = 'apple'
a.index('a')
>>
0
```



## 값 변경

> **.replace(old, new, count)**

바꿀 대상 글자를 새로운 글자로 바꿔서 반환한다.

count를 지정하면 해당 개수만큼만 시행한다.

```python
z = 'zoo!yoyo!'
z.replace(o, '', 2)
>>
'z!yoyo!'
```



> **.strip([chars])**

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나, 오른쪽을 제거한다.

- `.strip`
- `.lstrip()`

- `.rstrip()`

```python
# '\n' 개행도 공백에 포함되기 때문에 제거한다.
oh = '    oh!\n'
oh.strip()
>>
'oh!'
```

```python
escape = '\r\t\n'
escape.strip()
>>
''
```



> **.split()**

문자열을 특정한 단위로 나누어 리스트로 반환한다.

```python
csv = '1,Ryan,01012345678'
# 지정해주지 않으면 공백을 기준으로 나눈다.
csv.split(',')
>>
# type(list)
['1', 'Ryan', '01012345678']
```



> **'separator'.join(iterable)**

특정한 문자열로 만들어 반환한다.

반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐 join() 문자열로 반환한다.

```python
word = 'hihello'
' '.join(word)
>>
'h i h e l l o'
```

```python
words = ['hi', 'hello', 'ryan']
','.join(words)
>>
'hi,hello,ryan'
```





## 문자 변형

> **.capitalize() / .title() / .upper()**

- `.capitalize()` : 앞글자를 대문자로 만들어 반환한다.
- `.title()` :  apostropheㄴ 공백 이후를 대문자로 만들어 반환한다.
- `.upper()` : 모두 대문자로 만들어 반환한다.

```python
a = 'hI! Everyone, I\'m ryan'
```

```python
a.capitalize()
>>
"Hi! everyone, i'm ryan"
```

```python
a.title()
>>
"Hi! Everyone, I'M Ryan"
```

```python
a.upper()
>>
"HI! EVERYONE, I'M RYAN"
```



> **.lower() / .swapcase()**

- `lower()` : 모두 소문자로 만들어 반환한다.
- `swapcase()` : 대소문자를 서로 변경하여 반환한다.

```python
a = 'hI! Everyone, I\'m ryan'
```

```python
a.lower()
>>
"hi! everyone, i'm ryan"
```

```python
a.swapcase()
>>
"Hi! eVERYONE, i'M RYAN"
```



## 기타 문자열 관련 검증 Method : True / False return

> **.isalpha() / .isdecimal() / .isdigit() / .isnumeric()**
>
> **.isspace() / .isupper() / .istitle() / .islower()**

```python
'3'.isalpha()
>>
False
```

```python
'3.5'.isdecimal()
>>
False
```

```python
'3'.isnumeric()
>>
True
```



## 리스트(List)

> **변경가능하고(mutable)** / **순서가 있고(ordered)** / **반복 가능한(iterable)**

- 데이터 구조의 리스트(list)와 조작법(method)
  - https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists



## 값 추가 및 삭제

> **.append()**

리스트에 값을 추가할 수 있다.

```python
cafe = ['starbucks']
print(cafe)
>>
['starbucks']
```

```python
cafe.append('banapresso')
>>
['starbucks', 'banapresso']
```



> **.extend(iterable)**

리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있다.

```python
cafe = ['starbucks']
# 문자열을 하나씩 펼쳐서 요소로 담는다.
cafe.extend(['ediya'])
>>
['starbucks', 'banapresso', 'e', 'd', 'i', 'y', 'a']
```

```python
# .append()와 같은 기능을 한다.
cafe += ['angelinus']
>>
['starbucks', 'e', 'd', 'i', 'y', 'a', 'angelinus']
```



> **.insert(index,  element)**

정해진 위치 i에 값을 추가한다.

```python
# 0번째 index에 'hi'를 추가한다.
cafe = ['starbucks']
cafe.insert(0, 'hi')
>>
['hi', 'starbucks']
```

```python
# i가 -1 이면 뒤에서 두번째 index에 추가된다.
cafe.insert(-1, 'bye?')
>>
['hi', 'bye?', 'starbucks']
```

```python
# 길이를 넣어주면 마지막 index에 추가된다.
# list의 길이를 넘어서는 index를 지정해도 마지막에 추가된다.
cafe.insert(len(cafe), 'truley bye')
>>
['hi', 'starbucks', 'truley bye']
```



> **.remove()**

리스트에서 **값**을 삭제한다.

```python
# 해당 값을 찾아서 삭제하고, 값이 없으면 error 출력
numbers = [1, 2, 3, 1, 2]
numbers.remove(1)
print(numbers)
>>
[2, 3, 1, 2]
```



> **.pop(index)**

정해진 위치 i 에 있는 값을 삭제하고, 그 항목을 반환한다.

```python
# i가 지정되지 않으면 '마지막 항목'을 삭제하고 반환한다.
a = [1, 2, 3, 4, 5, 6]
a.pop(0)
>>
[2, 3, 4, 5, 6]
```

```python
# .pop()은 값이 return되기 때문에 별도의 값에 저장할 수 있다.
alphabet = ['a', 'b', 'c']
x = alphabet.pop()
print(x, alphabet)
>>
c ['a', 'b']
```



> **.clear()**

리스트의 모든 항목을 삭제한다.

```python
a = [1, 2, 3]
a.clear()
print(a)
>>
[]
```





## 탐색 및 정렬

> **.index()**

해당 값을 찾아 index를 반환한다.

```python
# 찾는 값이 없으면 error 출력
a = [1, 2, 3, 4, 5]
a.index(5)
>>
4
```



> **.count()**

원하는 값의 개수를 확인할 수 있다.

```python
a = [1, 2, 5, 1, 5, 1]
a.count(1)
>>
3
```

```python
# .count()를 사용해서도 range설정이 가능하다.
a = [1, 2, 5, 1, 5, 1]
for i in range(a.count(1)):
    a.remove(1)
print(a)
>>
[2, 5, 5]
```



> **.sort()**

정렬을 한다. 내장함수 sorted()와는 다르게 원본 list 자체를 변형시키고, None을 반환한다.

```python
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)
>>
[33, 1, 2, 4, 19, 20]
```

```python
# .sort()는 원본을 바꿔버림
lotto.sort()
print(lotto)
>>
[1, 2, 4, 19, 20, 33]
```

```python
# 원본은 그대로고 return만 바뀜
sorted(lotto)
>>
[1, 2, 4, 19, 20, 33]
```



> **.reverse()**

반대로 뒤집는다. 정렬 되는것은 아니다.

```python
friends = ['ryan', 'jordy', 'con', 'scappy']
friends.reverse()
>>
['scappy', 'con', 'jordy', 'ryan']
```



## 리스트 복사

```python
original_list = [1, 2, 3, 4]
copy_list = original_list
print(copy_list)
>>
[1, 2, 3, 4]
```

```python
# 복사한 리스트의 0번째 index를 'A'로 바꾸고 두 리스트 모두 출력해본다.
copy_list[0] = 'A'
print(copy_list, original_list)
>>
# copy_list를 바꿨음에도 불구하고 original_list의 값도 변했다.
['A', 2, 3, 4] ['A', 2, 3, 4]
```

```python
# 두 리스트의 id값이 같다.
print(id(original_list))
print(id(copy_list))
>>
1926164105728
1926164105728
```



## 리스트 복사 방법

> **slice 연산자 사용 [:]**

```python
# slice연산자로 복사하면 id값이 달라진다.
a = [1, 2, 3, 4]
b = a[:]
print(id(a))
print(id(b))
>>
1926163885824
1926164952384
```



> **list()** 활용

기존 list를 새로운 list로 형변환 한다.

```python
# 새로운 list로 형변환 하면 id값이 달라진다
a = [1, 2, 3, 4]
b = list(a)
print(id(a))
print(id(b))
>>
1926165030144
1926165019840
```



- 하지만, 이렇게 하는 것도 일부 상황에만 서로 다른 얕은 복사(shallow copy)이다.

- 만일 중첩된 상황에서 복사를 하고 싶다면, `깊은 복사(deep copy)`를 해야한다.

  즉, 내부에 있는 모든 객체까지 새롭게 값이 변경된다.



## List Comprehension

> List Comprehension은 표현식과 제어문을 통해 리스트를 생성한다.
>
> 여러 줄의 코드를 한 줄로 줄일 수 있다.



활용법

- ```python
  [expression for 변수 in iterable]
  ```

- ```python
  list(expression for 변수 in iterable)
  ```



## 세제곱 리스트

> 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`를 작성하시오.

```python
# 반복문을 사용
cubic_list = []
# 1~10까지 반복
for number in range(1, 11):
    # number의 세제곱을 리스트에 추가한다.
    cubic_list.append(number ** 3)
print(cubic_list)
>>
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

```python
# 조건표현식
[number**3 for number in range(1, 11)]
>>
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```



## List Comprehension + 조건문

> **조건문에 참인 식으로 리스트를 생성한다.**



활용법

- ```python
  [expression for 변수 in iterable if 조건식]
  ```

- ```python
  [expression if 조건식 else 식 for 변수 in iterable]
  ```

- else 조건이 들어가면 조건이 조건표현식 뒤쪽에 있어야한다.

## 짝수 리스트

> - 1~10까지의 숫자중 짝수만 담긴 리스트 `even_list`
> - 여러개의 `for` 혹은 `if`문을 중첩적으로 사용 가능하다.

```python
# 반복문 활용
even_list = []
# 1~10까지 반복
for i in range(1, 11):
    # 2로 나눈 나머지가 0이면 리스트에 추가
    if i % 2 == 0:
        even_list.append(i)
print(even_list)
>>
[2, 4, 6, 8, 10]
```

```python
# 조건표현식
[i for i in range(1, 11) if i % 2 == 0]
>>
[2, 4, 6, 8, 10]
```



## 피타고라스의 정리

> 주어진 조건(x < y < z < 20) 내에서 피타고라스 방정식의 해를 찾으세요.

```python
# 반복문 활용
result = []
# 1~20까지 x가 반복
for x in range(1, 20):
    # 1~20까지 y가 반복
    for y in range(x, 20):
        # 1~20까지 z가 반복
        for z in range(y, 20):
            # 피타고라스의 정리에 일치하면 리스트에 추가
            if x ** 2 + y ** 2 == z ** 2:
                result.append((x, y, z))
print(result)
>>
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
```

```python
# 조건표현식
[[(x, y, z)] for x in range(1, 20) for y in range(x, 20) for z in range(y, 20) if x**2 + y**2 == z**2]
print(result)
>>
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
```



## 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하세요.

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'
result = []
# words내에서 반복
for word in words:
    # 문자가 vowels 안에 없으면 result(list)에 더한다.
    if word not in vowels:
        result.append(word)
# result(list)에서 공백을 제거하고 string으로 변환
# list는 .split()을 사용할 수 없기 때문이다.
a = ''.join(result)
# 공백을 제거
b = a.split()
# 다시 문자열로 합친다.
c= ''.join(b)
print(c)
>>
Lfstshrt,yndpythn!
```



## 데이터 구조에 적용가능한 Built-in Function

순회 가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> **iterable  - list, dict, set, str, bytes, tuple, range**

- map()
- filter()
- zip()
- reduce()



>  **map(function, iterable)**

- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다.

- return은 `map_object` 형태이다.

```python
# 세제곱의 결과를 나타내는 함수 cube()
def cube(n):
    return n ** 3
```

```python
numbers = [1, 2, 3]
new_numbers = list(map(cube, numbers))
print(new_numbers)
>>
[1, 8, 27]
```



## 코딩 테스트의 기본

> **두 정수를 입력 받아 더한 값을 출력하시오.**

```python

a, b = map(int, a.split())
print(a + b)
>>
> 3 5
8
```



> **filter(function, iterable)**

- iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환한다.

- `filter object` 를 반환한다.

```python
# list에서 홀수만 걸러내는 코드를 작성하시오.
def odd(n)
return n % 2
```

```python
# numbers(list)에서 홀수인 요소만 걸러서 new_numbers(list)에 더한다.
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(filter(odd, numbers))
print(new_numbers)
>>
[1, 3, 5]
```



> **zip(*iterables)**

- 복수의 iterable 객체를 모아(`zip()`)준다.

- 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
pair = list(zip(girls, boys))
print(pair)
>>
[('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

