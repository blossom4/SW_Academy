# 06_Practice

> Data Structure



## 1. 썩은 과일 찾기

> 과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있다.
>
> (과일 봉지는 리스트를 의미한다.)
>
> 썩은 과일 조각들을 모두 신선한 것으로 교체하는 함수 `change_rotten_fruit()`를 작성하시오.



**유의**

- 만약 리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환한다.
- 반환된 리스트의 요소는 모두 소문자여야 한다.



```python
def change_rotten_fruit(fruit_bag):
    fresh = []
    # 주어진 과일가방 리스트 안에서 반복
    for i in fruit_bag:
        # 리스트의 요소중에서 'rotten'을 만나면 ''공백으로 수정
        fruits = i.replace('rotten', '')
        # 수정한 문자열을 모두 소문자로 바꿔서 fresh리스트에 추가
        fresh.append(fruits.lower())   
    # fresh 리스트 반환
    return fresh
```

```python
print(change_rotten_fruit([]))
print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
>>
[]
['apple', 'banana', 'apple']
['apple', 'banana', 'apple', 'grape']
```



___

## 2. 중복되지 않은 숫자의 합

> 같은 숫자가 한개 있거나 두개가 들어있는 리스트가 주어진다. 이러한 리스트에서 숫자가 한개만 있는 요소들의 합을 구하는 함수 `sum_of_repeat_number()`를 작성하시오.
>
> 예를 들어, `[4, 5, 7, 5, 4, 8]`는 7과 8이 한번만 나오기 때문에 두개를 더한 15가 결과값으로 도출된다.



```python
def sum_of_repeat_number(numbers):
    # number(list)를 set함수를 이용해 중복된 요소 제거
    my_set = set(numbers)
    res = 0
    # my_set(list)에서 반복
    for i in my_set:
        # numbers(list)에서 count가 1인 요소만 res에 더한다.
        if numbers.count(i) == 1:
            res += i
    return res
```

```python
print(sum_of_repeat_number([4, 4, 7, 8, 10]))
>>
25
```



___

