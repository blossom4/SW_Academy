# 03_Practice

> Function



## 1. 종합소득세 계산하기

> A라는 나라에서 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용된다.
>
> 즉, 1300만원을 벌었을 경우 `1,200 * 0.06 + 100 * 0.15`를 계산한 결과가 납부해야하는 세액이다.
>
> 세금의 결과를 반환하는 함수 `tax()`를 작성하시오.



| 과세표준액    | 세율 |
| ------------- | ---- |
| 1,200 이하    | 6%   |
| 1,200 ~ 4,600 | 15%  |
| 4,600 ~       | 35%  |

```python
def tax(won):
    # 1,200만원 이하면 6%적용
    if won <= 1200:
        return won * 0.06
    # 1,200만원은 6% 적용, 나머지 금액은 15% 적용
    elif won > 1200 and won <= 4600:
        return 1200 * 0.06 + (won - 1200) * 0.15
    # 1,200만원 6% 적용, 3,400만원 15%적용, 나머지 35% 적용
    else:
        return 1200 * 0.06 + 3400 * 0.15 + (won - 4600) * 0.35
```

```python
print(tax(1200))
print(tax(4600))
print(tax(5000))
>>
72.0
582.0
722.0
```



___

## 2. 문자열 탐색

> 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고, 주어진 문자열의 
>
> 첫번째와 마지막 문자가 같은 문자열의 수를 카운트하는 함수 `start_end()`를 작성하시오.



```python
def start_end(words):
    cnt = 0
    # words(list) 내에서 반복
    for i in words:
        # 문자열 길이가 2보다 작으면 다음 반복으로 넘어간다.
        if len(i) < 2:
            continue
        # 0번째 글자와 뒤에서 첫번째 글짜가 같으면 cnt +1
        if i[0] == i[-1]:
            cnt += 1
    # cnt 반환
    return cnt
```

```python
print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))
>>
3
```



___

## 3. Collatz 추측

> 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 
>
> 모든 수를 1로 만들 수 있다는 추측이다. 그 원리는 아래와 같다.
>
> 1. 입력된 수가 짝수이면 2로 나눈다.
> 2. 입력된 수가 홀수이면 3을 곱하고 1을 더한다.
> 3. 결과로 나온 수에 같은  작업을 1이 될 때까지 반복한다.
>
> 위 작업을 몇 번 반복해야하는지 반환하는 함수 `collatz()`를 작성하시오.
>
> (단, 작업을 500번 반복해도 1이 되지 않는다면 -1을 반환하시오.)



```python
def collatz(num):
    cnt = 0
    # num이 1이 될 때까지 반복
    while num != 1:
        # num이 현재 홀수일 경우 num*3 +1 
        if num % 2:
            num = num * 3 + 1
        # num이 현재 짝수일 경우 num/2
        else:
            num /= 2
        # 반복과정 한번 당 cnt +1
        cnt += 1
        # cnt가 500을 넘을 경우 -1 반환
        if cnt > 500:
            return -1
    # cnt 반환
    return cnt
```

```python
print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))
>>
8
4
111
-1
```



___

## 4. 회문 판별

> 회문 또는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열 등을 말한다.
>
> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어가 회문이면 True 회문이 아니면 False를 반환하는 함수를 작성하시오.
>
> 이때, 반복문(`while`)과 재귀 함수를 사용해서 각각 작성하시오.



```python
# iterative
def is_pal_while(word):
    # 문자열의 앞과 뒤를 한쌍으로 이루어서 같은지 확인한다.
    for i in range(len(word) // 2):
        # 같을 경우 계속 반복진행
        if word[i] == word[-i - 1]:
            continue
        # 다른 쌍이 나타나는 순간 바로 False 반환
        else:
            return False
    # 같은 쌍이 끝까지 반복되서 반복이 끝나면 True 반환
    return True
```

```python
print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
>>
False
True
True
```



```python
# recursive
def is_pal_recursive(word):
    # 문자열의 앞과 뒤를 한쌍으로 이루어서 같은지 확인한다.
    for i in range(len(word) // 2):
        # 같을 경우 앞,뒤의 문자를 하나씩 잘라낸 나머지로 함수 호출
        if word[i] == word[-i - 1]:
            return is_pal_recursive(word[i + 1:-i])
        # 다른 쌍이 나타나는 순간 바로 False 반환
        else:
            return False
    # 같은 쌍이 끝까지 반복되서 반복이 끝나고 스택이 처리되면 True 반환
    return True
```

```python
print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
>>
False
True
True
```



___

