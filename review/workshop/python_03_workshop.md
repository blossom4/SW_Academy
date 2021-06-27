# python_03_workshop

> Function



## 1. List의 합 구하기

> 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.



```python
def list_sum(numbers):
    total = 0
    # numbers(list)에서 반복
    for n in numbers:
        total += n
    return total
list_sum([1, 2, 3, 4, 5])
>>
15
```



___

## 2. Dictionary로 이루어진 List의 합 구하기

> Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 `dict_list_sum` 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.



```python
def dict_list_sum(infos):
    total = 0
    # infos(dict)에서 반복
    for info in infos:
        # infos에서 'age'의 value값을 뽑아 total에 더한다.
        total += info.get('age')
    # total 반환
    return total
dict_list_sum([
    {'name': 'kim', 'age': 12},
    {'name': 'lee', 'age': 4}
])
>>
16
```



___

## 3. 2차원 List의 전체 합 구하기

> 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.



```python
def all_list_sum(lists):
    total = 0
    # lists(list)에서 반복
    for l in lists:
        # lists의 요소(list)에서 반복
        for i in l:
            total += i
    # total 반환
    return total
list_res = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
]
all_list_sum(list_res)
>>
55
```



___

