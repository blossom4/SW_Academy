# 04_Practice

> Complex Data Structure
>
> Iterative Statement of Two-Dimensional List



## 1. 복잡한 리스트의 합

> 2차원 리스트를 반복하는 방법을 알아봅시다.



주어진 아래의 리스트를 반복하여 숫자의 합을 반환하시오.

```python
numbers = [
    [1, 4],
    [10, 5],
    [20, 30]    
]
```



- for 문을 활용하여 풀이하기

```python
def sum_list(numbers):
    total = 0
    # number(list)내에서 반복
    for element in numbers:
        # 요소들을 total에 더한다.
        total += sum(element)
    return total
```

```python
print(sum_list([[1, 4], [10, 5], [20, 30]]))
>>
70
```

- index로 접근하여 풀이하기

```python
def sum_list_index(numbers):
    res = 0
    # numbers(list)의 길이만큼 반복
    for i in range(len(numbers)):
        # numbers의 요소(list)의 길이만큼 반복
        for j in range(len(numbers[i])):
            # res에 더하여 저장
            res += numbers[i][j]       
    return res
```

```python
print(sum_list_index([[1, 4], [10, 5], [20, 30]]))
>>
70
```

- while 문을 활용하여 풀이하기

```python
def sum_list_while(numbers):
    res = 0
    i = 0
    # i가 numbers(list)의 길이보다 작을 때까지만 반복
    while i < len(numbers):
        # j 초기화
        j = 0
        # j가 numbers(list)의 길이보다 작을 때까지만 반복
        while j < len(numbers[i]):
            # res에 요소값을 더한다.
            res += numbers[i][j]
            j += 1
        i += 1
    return res
```

```python
print(sum_list_while([[1, 4], [10, 5], [20, 30]]))
>>
70
```



___

## 2. 시험 점수

> 2차원 배열



A반 학생들의 점수는 아래와 같고, students 리스트에 저장되어 있다.

- A학생(국어 100점, 수학 80점, 영어 100점)
- B학생(국어 90점, 수학 90점, 영어 60점)
- C학생(국어 80점, 수학 80점, 영어 80점)

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```



**학생별 출력**

- 아래의 리스트를 반복하여 **학생별 총합**을 순서대로 `출력`하시오.
- `sum` 함수 사용 금지

```python
# students(list)의 길이만큼 반복
for i in range(len(students)):
    res = 0
    # students의 요소(list)의 길이만큼 반복하면서 res에 더한다.
    for j in range(len(students[i])):
        res += students[i][j]
    print(res)
>>
280
240
240
```

**과목별 출력**

- 아래의 리스트를 반복하여 **과목별 총합**을 순서대로 `출력`하시오.
- `sum` 함수 사용 금지

```python
# students(list)의 길이만큼 반복
for i in range(len(students)):
    res = 0
    # students의 요소(list)의 길이만큼 반복
    for j in range(len(students[i])):
        # 각 요소의 같은 index 요소들끼리 더한다.
        res += students[j][i]
    print(res)
>>
270
250
240
```



___

