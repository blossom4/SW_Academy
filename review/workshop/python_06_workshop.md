# python_06_workshop

> Data Structure
>
> Method



## 1. 무엇이 중복일까

> 문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오.



```python
def duplicated_letters(word):
    # 입력받은 문자열 중 중복된 것을 제거
    word_m = set(word)
    res = []
    # 중복된 것이 제거된 문자열에서 반복
    for i in word_m:
        # 기존 문자열에서 count가 1이 아닌 문자는 res리스트에 추가
        if word.count(i) != 1:
            res.append(i)
    return res
```

```python
print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
>>
['p']
['n', 'a']
```



___

## 2. 소대소대

> 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.



```python
def low_and_up(word):

    res = []
    # 입력된 문자열 내에서 반복
    for i in range(len(word)):
        # 짝수번째 index의 해당문자는 대문자로 변환 후 리스트에 추가
        if i % 2:
            res.append(word[i].upper())  
        # 홀수번째 index의 해당문자는 소문자로 변환 후 리스트에 추가    
        else:
            res.append(word[i].lower())
    # 리스트 요소들을 합쳐서 반환        
    return ''.join(res)
```

```python
print(low_and_up('apple'))
print(low_and_up('banana'))
>>
aPpLe
bAnAnA
```



___

## 3. 숫자의 의미

> 정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남 기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 
>
> 이때, 제거된 후 남은 수들이 담 긴 list의 요소들은 기존의 순서를 유지해야 한다.



```python
def lonely(numbers):
    res = []
    # 입력된 숫자 리스트 길이 -1 만큼 반복 (두개씩 묶어서 비교할 것이므로)
    for i in range(len(numbers) - 1):
        # i번째 요소와 i+1번째 요소가 다르면 i번째 요소를 리스트에 추가
        if numbers[i] != numbers[i + 1]:
            res.append(numbers[i])
    # 맨 마지막 요소는 앞의 리스트 구성과 관계없이 무조건 추가
    res.append(numbers[i + 1])   
    return res
```

```python
print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
>>
[1, 3, 0, 1]
[4, 3]
```



___

