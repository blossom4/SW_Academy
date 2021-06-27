# python_06_homework

> Data Structure
>
> Method



## 1. Built-in function / Method

> sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.



```python
# 원본 데이터 자체를 바꾼다.
numbers = [1, 5, 12, 3, 7, 20, 4]
result = numbers.sort()
print(result)
print(numbers)
```

```python
# 원본 데이터는 바꾸지않는다.
numbers = [1, 5, 12, 3, 7, 20, 4]
result = sorted(numbers)
print(result)
print(numbers)
```



___

## 2. .extend() / .append()

> .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.



```python
# .extend()는 주어진 string을 펼쳐서 list에 담는다.
students = ['A', 'B', 'C']
students.extend('XYZ')
print(students)
>>
['A', 'B', 'C', 'X', 'Y', 'Z']
```

```python
# .append()는 주어진 string을 그대로 list에 담는다.
students = ['A', 'B', 'C']
students.append('XYZ')
print(students)
>>
['A', 'B', 'C', 'XYZ']
```



___

## 3. 복사가 잘 된 건가?

> 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

```python
# a(list)와 a를 저장한 b는 같은 주소를 참조하고 있기때문이다.
a = [1, 2, 3, 4, 5]
b = a
a[0] = 10
print(a)
print(b)
>>
[10, 2, 3, 4, 5]
[10, 2, 3, 4, 5]
```



___

