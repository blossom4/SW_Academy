# python_02_workshop

> Data / Control Statement



## 1. 간단한 N의 약수

> 입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.



```python
N = int(input())
res = ''
# 1~N까지 반복
for i in range(1, N + 1):
    # N이 index로 나누어 떨어지면 res(string)에 더한다.
    if N % i == 0:
        res += str(i)
print(res)
>>
> 6
1236
```



___

## 2. 중간값 찾기

> 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.



```python
n = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
# n(list)의 길이 -1 까지 반복
for i in range(len(n) - 1):
    # 앞의 index 요소가 더 작으면 swap
    if n[i] > n[i + 1]:
        temp = n[i]
        n[i] = n[i + 1]
        n[i + 1] = temp
# 최종 정렬 후 중간 index 출력
print(n[len(n) // 2])
>>
80
```



___

## 3. 계단 만들기

> 자연수 number를 입력 받아, 아래와 같이 높이가 number인 내려가는 계단을 출력하시오.



```python
N = int(input())
# 1~N까지 반복
for i in range(1, N + 1):
    # 1~N까지 반복하면서 각각 1~i까지 반복
    for j in range(1, i + 1):
        # 반복이 모두 끝났을 때만 개행
        print(j, end = ' ')
    print()
>>
> 4
1 
1 2 
1 2 3 
1 2 3 4 
```



___

