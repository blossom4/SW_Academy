# 07_Data_Structure2

> **알고리즘에 자주 활용되는 순서가 없는 (unordered) 데이터 구조**

- Set
- Dictionary



## Set

> 변경가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)



데이터 구조로서의 set와 조작법(method)

- https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset



## 추가 및 삭제

> **.add(element)**

element를 set에 추가한다.

```python
# 순서가 존재하지 않는다.
a= {'apple', 'banana', 'watermelon'}
a.add('kiwi')
>>
{'kiwi', 'apple', 'banana', 'watermelon'}
```



> **.update(*others)**

여러가지 값을 추가한다. 그리고 인자로 반드시 iterable한 데이터 구조를 전달해야한다.

```python
# 순서도 존재하지 않고, 중복도 허용하지 않는다.
a= {'apple', 'banana', 'watermelon'}
a.update('kiwi')
>>
{'k', 'i', 'watermelon', 'w', 'banana', 'apple'}
```



> **.remove(element)**

element를 set에서 삭제하고,  삭제할 요소가 없을경우 KeyError가 발생한다.

```python
a= {'apple', 'banana', 'watermelon'}
a.remove('apple')
>>
{'banana', 'watermelon'}
```



> **.discard(element)**

element를 set에서 삭제하고, 요소가 없어도 Error가 발생하지 않는다.

```python
a= {'apple', 'banana', 'watermelon'}
a.discard('apple')
>>
{'banana', 'watermelon'}
```



> **.pop()**

임의의 원소를 제거해 반환한다.

```python
a= {'apple', 'banana', 'watermelon'}
a.pop()
>>
{'banana', 'watermelon'}
```



## Dictionary

> **변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)**
>
> `Key: Value` 페어(pair)의 자료구조



데이터 구조로서의 딕셔너리(dictionary)와 조작법(method)

- https://docs.python.org/ko/3/library/stdtypes.html#mapping-types-dict



## 조회

> **.get(key[, default])**

key를 통해 value를 가져오며, 절대로 KeyError가 발생하지 않는다. defualt는 기본적으로 None이다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.get('apple')
>>
'apple'
```

```python
# my_dict.get('pineapple', value)
# 찾는 요소가 없으면 value를 반환한다.
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.get('pineapple')
>>
None
```



## 추가 및 삭제

> **.pop(key[, default])**

key가 딕셔너리에 있으면 제거하고 그 값을 돌려준다. 그렇지 않으면 default를 반환한다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생한다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')
>>
'사과'
```

```python
# my_dict.pop('pineapple', value)
# 찾는 요소가 없으면 value를 반환한다.
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('pineapple')
>>
KeyError
```



> **.update()**

값을 제공하는 key, value로 덮어쓴다.ㅣ

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update({'banana' : '빠나나'})
>>
{'apple': '사과', 'banana': '빠나나', 'melon': '멜론'}
```

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(melon = '메론')
>>
{'apple': '사과', 'banana': '바나나', 'melon' : '메론'}
```





## 딕셔너리 순회(반복문 활용)

딕셔너리에 `for` 문을 실행하면 기본적으로 다음과 같이 동작합니다.

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)
>>
john
eric
justin
```

딕셔너리의 **key**를 접근할 수 있으면 **value**에도 접근할 수 있기 때문이다.

따라서 딕셔너리의 value를 출력하기 위해서는 아래와 같이 작성한다.

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)
# key값 출력
print(grades.keys())
# value값 출력
print(grades.values())
# key와 value값을 묶어서 출력
print(grades.items())
>>
dict_keys(['john', 'eric', 'justin'])
dict_values([80, 90, 90])
dict_items([('john', 80), ('eric', 90), ('justin', 90)])
```

