# 01_Data_container



# 컨테이너(Container)



여러 개의 값을 저장할 수 있는 것

- Sequence type : ordered data
- Non-sequence type : undered data



## Sequence type Container

`sequence`는 데이터가 순서대로 나열된(ordered) 형식을 나타낸다.

- 단, 순서대로 나열된 것이 정렬되었다(sorted)라는 **뜻은 아니다.**



> 특징

1. 순서를 가질 수 있다.
2. 특정 위치의 데이터를 가리킬 수 있다.



> 종류

python의 기본적인 sequence type.

- 리스트(list)
- 튜플(tuple)
- 레인지(range)
- 문자형(string)
- 바이너리(binary)



## 리스트(`list`)

- 리스트는 대괄호 `[]`와 `list()`로 만들 수 있다.
- 값에 접근할 때는 `list[i]`를 사용한다.
- list의 이름을 `list`라고 만들면 안된다.



```python
# make list
my_list = ['h', 'i']
my_list2 = [1, 2]
another_list = list(my_list2)
print(my_list, type(my_list))
print(another_list, type(another_list))
>>
['h', 'i'] <class 'list'>
[1, 2] <class 'list'>
```

```python
a_list = [1, 2, 3]
print(a_list[0])
>>
1
```



## 튜플(`tuple`)

- 튜플은 리스트와 유사하지만, `()` 로 묶어서 표현한다.
- 그리고 tuple은 수정할 수 없고(immutable), 읽기만 가능하다.

```python
my_tuple = (1, 2)
print(my_tuple, type(my_tuple))
>>
(1, 2) <class 'tuple'>
```

```python
# empty tuple
empty = ()
print(len(empty), type(empty))
>>
0 <class 'tuple'>
```

```python
# single tuple > ,
single_tuple = ('hi',)
print(len(single_tuple), type(single_tuple))
>>
1 <class 'tuple'>
```



## 레인지(`range()`)

`range`는 숫자의 seuquence를 나타내기 위해 사용된다.

- 기본형 : `range()`
  - `0 ~ (n - 1)` 까지 값을 가진다.

- 범위지정 : `range(n, m)`
  - `n ~ (m - 1)`까지 값을 가진다.
- 범위 및 스텝 지정 : `range(n, m, s)`
  - `n ~ (m - 1)`까지 +S만큼 증가한다.

```python
list(range(3))
>>
[0, 1, 2]
```



## Sequence에서 활용할 수 있는 연산자 / 함수

연산자, 함수	/	내용

- a `in` b	       >	containment test
- a `not in` b   >    containment test
- s1 `+` s2          >    concatenation
- s `*` n              >    n번 반복하여 더하기
- `s[i]`              >    indexing
- `s[i:j]`          >    slicing
- `s[i:j:l]`      >    k 간격으로 slicing
- `len(s)`          >    길이
- `min(s)`          >    최소값
- `max(s)`          >    최대값
- `s.count(x)`  >    x의 개수 

```python
# containment test
str = 'hi, ryan'
print('t' in str)
>>
False
```

```python
# concatenation
print('hi, ' + 'ryan')
print((1, 2) + (3, 4))
>>
hi, ryan
(1, 2, 3, 4)
```

```python
# indexing / slicing
alphabet = ['a', 'b', 'c', 'd', 'e']
print(alphabet[2])
print(alphabet[2:])
>>
c
['c', 'd', 'e']
```



## Non - sequence type Container

- 셋(set)
- 딕셔너리(dictionary)



## 셋(`set`)

`set`은 **순서가 없는** 자료구조이다.

- `set`은 수학의 집합과 같게 처리된다.
- `set`은 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.
- 빈 집합을 만들때는 `set()`을 사용해야한다. (`{}`사용 불가능)

```python
set_a = {1, 2, 3}
print(set_a)
print(type(set_a))
>>
{1, 2, 3}
<class 'set'>
```

```python
# 중복된 값 제거
list_a = [1, 2, 3, 1, 1, 2]
set(list_a)
>>
{1, 2, 3}
```



## 딕셔너리(`dictionary`)

`dictionary`는 **`key`와 `value`**가 쌍으로 이루어져있는 궁극의 자료구조이다.

`{key1 : value1, key2 : value2, key3 : value3, ...}`

- `{}`를 통해 만들며, `dict()`로 만들 수도 있다.

- `key`는 변경 불가능(immutable)한 데이터만 가능하다.

  `immutable : string, integer, float, boolean, tuple, range`

- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.

```python
dict_a = {}
print(dict_a, type(dict_a))
dict_b = dict()
print(dict_b, type(dict_b))
>>
{} <class 'dict'>
{} <class 'dict'>
```

```python
# dictionary는 중복된 key는 존재할 수가 없다.
# 마지막에 입력된 정보로 덮어씌워진다.
my_dict = {'ryan' : '남', 'ryan' : '여'}
my_dict
>>
{'ryan': '여'}
```

```python
# dictionary
phone = {'서울' : '02', '경기' : '031'}
```

```python
# index가 아닌 key로 접근한다.
phone['경기']
>>
'031'
```

```python
# .keys()
phone.keys()
>>
dict_keys(['서울', '경기'])
```

```python
# .values()
phone.values()
>>
dict_values(['02', '031'])
```

```python
# .items()
phone.items()
>>
dict_items([('서울', '02'), ('경기', '031')])
```

```python
# 리스트의 형태를 띄고있지만 실제 리스트는 아니다.

print(phone.items())
print(type(phone.items()))
>>
dict_items([('서울', '02'), ('경기', '031')])
<class 'dict_items'>
```

```python
# (key, value)가 튜플로 묶인 원소들로 만들어져있다.
# type은 튜플이다.

print(list(phone.items())[0])
print(type(list(phone.items())[0]))
>>
('서울', '02')
<class 'tuple'>
```



## Container type transition

> python에서 container는 서로 변환할 수 있다.

![container type](Data_container_01.assets/container type.png)



## 데이터의 분류

>  mutable VS immutable

데이터는 크게 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)으로 나뉘며, phyton은 각각을 다르게 다룬다.



## 변경 불가능한(`immutable`)데이터

- 리터럴(literal)
  - 숫자(number)
  - 문자(string)
  - 참/거짓(bool)
- 레인지(`range()`)
- 튜플(`tuple()`)
- 프로즌셋(`frozenset()`)



## 변경 가능한(`mutable`)데이터

- 리스트(`list`)
- 딕셔너리(`dict`)
- 셋(`set`)

```python
# mutable 데이터의 복사
# num1과 num2는 같은 리스트를 가리킨다.
num1 = [1, 2, 3, 4]
num2 = num1
num2[0] = 100

print(num1)
print(num2)
>>
[100, 2, 3, 4]
[100, 2, 3, 4]
```

```python
# 따라서, 한 리스트의 값만 변경하고 싶다면 따로 리스트에 저장해두고 변경해야한다.

num1 = [1, 2, 3, 4]
num2 = list(num1)
num2[0] = 100

print(num1)
print(num2)
>>
[1, 2, 3, 4]
[100, 2, 3, 4]
```







