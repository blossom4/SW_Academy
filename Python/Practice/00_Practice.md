# 00_Practice

> Data / Control Statement



## 1. 개수 구하기

> 주어진 리스트의 요소는 학생 이름으로 이루어져 있다. 학생들의 수를 출력하시오.



```python
students = ['jo', 'max', 'ryan']
cnt = 0
# students(list) 길이만큼 반복
for i in list(students):
    # students 요소를 하나씩 만날때 마다 cnt +1
    cnt += 1
# cnt 출력
print(cnt)
>>
3
```

```python
# built-in function
len(students)
>>
3
```



---

## 2. 득표수 구하기

> 주어진 리스트는 반장 선거투표 결과이다. ryan의 총 득표수를 출력하시오.



```python
students = ['ryan', 'jo', 'ryan', 'max', 'jo', 'cho', 'ryan', 'you']
cnt = 0
# students(list) 길이 만큼 반복
for i in range(8):
    # students의 요소가 'ryan'일 때 cnt +1
    if students[i] == 'ryan':
        cnt += 1
# cnt 출력
print(cnt)
>>
3
```

```python
# built-in function
students.count('ryan')
>>
3
```



---

## 3. 최대값 구하기

> 주어진 리스트의 요소 중에서 최대값을 출력하시오.



```python
numbers = [7, 10, 22, 4, 3, 17]
# numbers(list) 길이만큼 반복
for i in range(len(numbers) - 1):
    # 앞의 요소가 뒤의 요소보다 크면 swap
    if numbers[i] > numbers[i + 1]:
        # 오름차순으로 정렬
        temp = numbers[i]
        numbers[i + 1] = temp
        numbers[i] =numbers[i + 1]
# numbers의 마지막 index 출력
print(numbers[len(numbers) - 1])
>>
22
```

```python
# built-in function
max(numbers)
>>
22
```



---

## 4. 최소값 구하기

> 주어진 리스트의 요소 중에서 최소값을 출력하시오.



```python
numbers = [7, 10, 22, 4, 3, 17]
# numbers(list) 길이만큼 반복
for i in range(len(numbers) - 1):
    # 앞의 요소가 뒤의 요소보다 작으면 swap
    if numbers[i] < numbers[i + 1]:
        # 내림차순으로 정렬
        temp = numbers[i]
        numbers[i + 1] = temp
        numbers[i] =numbers[i + 1]
# numbers의 마지막 index 출력
print(numbers[len(numbers) - 1])
>>
3
```

```python
# built-in function
min(numbers)
>>
3
```



---

## 5. 최대값과 등장 횟수 구하기

> 주어진 리스트의 요소 중에서 최대값과 등장 횟수를 출력하시오.



```python
numbers = [7, 10, 22, 7, 22, 22]
cnt = 0
# numbers(list) 길이만큼 반복
for i in range(len(numbers) - 1):
    # 앞의 요소가 뒤의 요소보다 크면 swap 
    if numbers[i] > numbers[i + 1]:
        # 오름차순으로 정렬
        temp = numbers[i]
        numbers[i + 1] = temp
        numbers[i] =numbers[i + 1]
# 오름차순으로 정렬된 numbers(list) 길이만큼 반복
for j in range(len(numbers) - 1):
    # numbers 요소들 중 최대값인 마지막 index와 값이 같을 경우 cnt +1
    if numbers[j] == numbers[len(numbers) - 1]:
        cnt += 1
# cnt 출력
print(numbers[len(numbers) - 1], cnt)
>>
22 3
```



---

## 6. 5의 개수 구하기

> 주어진 리스트의 요소 중에서 5의 개수를 출력하시오



```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0
# numbers(list) 길이만큼 반복
for i in range(10):
    # numbers 요소 중 5와 같은 값이 있으면 cnt +1
    if numbers[i] == 5:
        cnt += 1
# cnt 출력
print(cnt)    
>>
3
```

```python
# built-in function
numbers.count(5)
>>
3
```



---

## 7. 'a'가 싫어

> 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력하시오.



```python
word = input()
# 입력받은 word의 길이만큼 반복
for i in range(len(word)):
    # word의 요소가 'a'가 아니면 출력
    if word[i] != 'a':
        print(word[i], end = '')
>>
> banana
bnn
```

```python
# ver.2
word = input()
# 입력받은 word 내에서 반복
for i in word:
    # word의 요소가 'a'가 아니면 출력
    if i != 'a':
        print(i, end = '')
>> 
> banana
bnn
```



---

## 8. 단어 뒤집기

> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.



```python
word = input()
# 입력받은 word의 길이만큼 반복
for i in range(len(word)):
    # word의 마지막 index부터 차례대로 출력
     print(word[len(word) - i - 1], end = '')
>>
> asdf
fdsa
```

```python
# ver.2
word = input()
result = ''
# 입력받은 word 내에서 반복
for char in word:
    # word 내의 문자를 result에 차례대로 더해서 저장
    result = char + result
# result 출력
print(result)
>>
> asdf
fdsa
```



---



