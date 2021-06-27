# python_01_workshop

> Data / Control Statement



## 1. 세로로 출력하기

> 자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.



```python
number = int(input())
# 1~number까지 반복하면서 index를 출력
for i in range(1, number + 1):
    print(i)
>>
> 5
1
2
3
4
5
```



___

## 2. 거꾸로 세로로 출력하기

> 자연수 number를 입력 받아, number부터 1까지의 수를 세로로 한줄씩 출력하시오.



```python
number = int(input())
# number만큼 반복하면서 number에서 index를 뺀 값을 출력
for i in range(number):
    print(number - i)
>>
> 5
5
4
3
2
1
```



___

## 3. N줄 덧셈

> 입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값을 출력하시오. (단, 주어지는 숫자는 10000을 넘지 않는다. )



```python
number = int(input())
res = 0
# number만큼 반복하면서 index를 res에 더한 값을 출력
for i in range(number + 1):
    res += i
print(res)
>>
> 5
15
```



___

