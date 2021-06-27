# 01_Practice

> Function



## 1. abs() 직접 구현하기

> 절대값은 숫자형 자료(int, float)가 들어오면 절대값을 반환하고, 
>
> 복소수형 자료(complex)가 들어오면 자료의 크기를 반환한다.



```python
def my_abs(x):
    # 입력받은 허수
    num = ''
    # 실수부
    real = ''
    # 허수부
    non_real = ''
    # +/- 기호를 만난것을 표시하는 flag
    flag = 0
    # 입력받은 수가 허수인지 판별
    if type(x) is complex:
        num += str(x)
        # 허수의 경우 (x + yj)의 형태로 반환되므로 앞의 '('와 뒤의 'j)'는 고정
        # 따라서, 고정된 부분을 제외하고 가운데 숫자 부분에서만 반복
        for i in range(1, len(num) - 2):
            # 실수부와 허수부를 구분하기 위해서, +/- 기호를 만나면 flag 변경
            if num[i] == '+' or num[i] == '-':
                flag = 1
            # +/- 기호를 만나기 전에(flag == 0) 숫자를 만나면 실수부 real에 저장
            # +/- 기호를 만난 후에(flag == 1) 숫자를 만나면 허수부 non_real에 저장
            if num[i] != '+' and num[i] !='-':
                if flag == 0:
                    real += num[i]
                if flag == 1:
                    non_real += num[i]
        # real과 non_real에 저장된 숫자문자를 int로 형변환해서 그 크기를 res에 저장
        res = (int(real) ** 2 + int(non_real) ** 2) ** (1/2)
        # res 반환
        return res
    else:
        # 양수이면 그대로 반환
        if x > 0:
            return x
        # 0과 0.0은 다른 객체이기 때문에 0을 제곱해서 float형으로 변환해서 반환
        elif x == 0:
            return 0 ** 2
        # 음수이면 -1을 곱해서 양수로 반환
        elif x < 0:
            return x * -1
print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))
>>
5.0
0.0
5
5.0 0.0 5
```

```python
# built-in function
def my_abs(x):
	# 입력받은 숫자 x가 허수인지 확인
    if type(x) == complex:
        # 허수가 맞다면 크기를 계산하여 반환
        return (x.real ** 2 + x.imag ** 2) ** (1 / 2)
    else:
        # x가 0이면 int형인 0에서 float형인 0.0으로 변환하여 반환
        if x == 0:
            return x ** 2
        # x가 양수면 그대로 반환
        elif x > 0:
            return x
        # x가 음수면 -1을 곱해서 반환
        elif x < 0:
            return x * -1
```

```python
print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))
>>
5.0
0.0
5
5.0 0.0 5
```



---

## 2. all() 직접 구현하기

> all()은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환한다.
>
> python 내장함수 all()을 직접구현한 my_all()을 작성하시오.



```python
def my_all(elements):
    # elements(list) 내에서 반복
    for i in elements:
        # 1. elements가 비어있을 경우에는 조건에 걸리지 않으므로 바로 True 반환
        # 2. 거짓인 요소를 만나 조건문에 들어가게되면, 바로 False를 반환 후 종료
        # 3. 끝까지 거짓인 요소가 없으면 반복문을 빠져나오고 True 반환
        if not i:
            return False
    return True
```

```python
print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))
>>
True
True
False
True True False
```



## 3. any() 직접 구현하기

> any는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고,
>
> 비어있으면 False를 반환한다.
>
> python 내장함수 any()를 직접 구현한 my_any() 함수를 작성하시오.



```python
def my_any(elements):
    # elements(list) 내에서 반복
    for i in elements:
        # 1. elements가 비어있을 경우 조건에 걸리지 않으므로 바로 False 반환
        # 2. 참인 요소를 만나 조건문에 들어가게되면 바로 True 반환
        # 3. 끝까지 참인 요소가 없으면 반복문을 빠져나오고 False 반환
        if i:
            return True
    return False
```

```python
print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))
>>
True
True
False
True True False
```



---

