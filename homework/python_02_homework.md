# python_02_homework

> Data / Control Statement



## 1. Mutable / Immutable

> 제시 된 컨테이너들을 각각, 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.



**Mutable**

- List
- Set
- Dictionary

**Immutable**

- String
- Tuple
- Range



___

## 2. 홀수 list

> range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.



```python
odd_list = []
# 1 ~ 50의 범위에서 반복
for i in range(1, 50):
    # 2로 나눈 나머지가 True(1)이면,
    if i % 2:
        # i//2 번째 위치에 i를 넣는다.
        odd_list.insert(i // 2, i)       
print(odd_list)
>>
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
```



___

## 3. Dictionary 생성

> 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.



```python
students_dict = {
    '영신' : 29,
    'youngshin' : 28,
    'Max' : 27,
}
print(students_dict)
>>
{'영신': 29, 'youngshin': 28, 'Max': 27}
```



___

## 4. 반복문으로 네모 출력

> 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 
>
> 별(*) 문자를 이용하여 출력하시오. (단, 반복문을 사용하여 작성하시오.)



```python
n = 5
m = 4
# 세로길이 m 만큼 반복
for j in range(m):
    # 가로길이 n 만큼 반복
    for i in range(n):
        # 끝에 ''을 넣어서 자동개행이 안되게 한다.
        print('*', end = '')
    # 가로길이만큼 반복이 되었으면, 개행을 한다.
    print()
>>
*****
*****
*****
*****
```



___

## 5. 조건 표현식

> 제시된 if 문을 조건 표현식으로 바꾸어 작성하시오.
>
> ```python
> temp = 36.5
> if temp >= 37.5:
>     print('입실 불가')
> else:
>     print('입실 가능')
> ```



```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
>>
입실 가능
```



___

## 6. list 평균값

> 제시된 list의 평균 값을 출력하시오.



```python
scores = [80, 89, 99, 83]
total = 0
# scores(list) 내에서 반복
for i in scores:
    # scores의 요소를 total에 더해나간다.
    total += i
# 총합을 scores(list)의 길이로 나눠서 평균 res를 구한다.
res = total / len(scores)
print(res)
>>
87.75
```



___

