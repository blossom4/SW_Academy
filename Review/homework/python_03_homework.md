# python_03_homework



## 1. Built-in 함수

> Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.



- abs()
- dict()
- bool()
- ascii()
- bin()



___

## 2. 정중앙 문자

> 문자열을 전달받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오.
>
> (단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.)



```python
def get_middle_char(str):
    even = ''
    i = len(str)
    # string의 길이 i가 홀수이면, i//2번째 문자를 반환
    if i % 2:
        return str[(i // 2)]
    # string의 길이 i가 짝수이면, (i//2-1)번째 문자와 그다음 문자 2개를 반환
    else:
        even += str[i // 2 - 1]
        even += str[i // 2]
        return even
```

```python
print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
>>
a
di
```



___

## 3. 위치 인자와 키워드 인자

> 다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.

```python
def info(name, location = 'Seoul'):
    print(f'{name}의 지역은 {location}입니다.')
# (1)
info('ryan')
# (2)
info(location = 'Daejeon', name = 'youngshin')
# (3)
info('jo', location = 'Busan')
# (4)
info(name = 'cho', 'Gwangju')
>>
(4)
```



___

## 4. 나의 반환값은

> 다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.



```python
def my_func(a, b):
    c = a + b
    return(c)
    result = my_func(3, 7)
print(result)
>>
10
```



___

## 5. 가변 인자 리스트

> 가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오.



```python
# 가변 인자들을 입력 받는다.
def my_avg(*args):
    total = 0
    # 입력받은 인자들의 길이만큼 반복하며 더한다.
    for i in args:
        total += i
    # 총합을 인자들의 개수로 나눈다.
    return total / len(args)
```

```python
print(my_avg(10, 1, 1))
print(my_avg(77, 83, 95, 80, 70))
>>
4.0
81.0
```



___







