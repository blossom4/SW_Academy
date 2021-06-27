# 05_Practice

> Data Structure



## 1. 모든 위치

> 주어진 문자열(text)에서 제시된 알파벳(alphabet)의 등장 위치를 리스트로 반환하시오. 
>
> 해당 알파벳이 등장하지 않으면, -1을 반환하시오.



```python
def my_find(text, alphabet):
    res = []   
    # text(list)의 길이만큼 반복
    for i in range(len(text)):
        # text의 i번째 요소가 alphabet과 같으면 res(list)에 추가
        if text[i] == alphabet:
            res.append(i)
    # 만약 res(list)가 요소가 존재하면 res 반환
    if res:
        return res
    # res(list)에 요소가 없으면 -1 반환
    else:
        return -1
```

```python
print(my_find('apple', 'p'))
print(my_find('a', 'p'))
>>
[1, 2]
-1
```



___

## 2. 출석 체크

> 주어진 학생 n과 출석한 학생명부 students 문자열이 있다. 결석한 학생들로 구성된 문자열을 반환하시오.
>
> n이 7일 때, 1 2 3 4 5 6 7의 출석 번호가 부여되고, '1 3 5'는 출석한 학생 명부이다.
>
> 즉, 결석한 학생 명부 '2 4 6 7'을 return 해야 한다.



```python
def check(n, students):
    # input받은 문자열들을 공백을 기준으로 잘라서 list로 합친다.
    attend = list(map(str, students.split()))
    every = []
    # 1~n까지 반복하면서 숫자를 문자로 변환하여 every(list)에 추가
    for i in range(1, n + 1):
        every += [str(i)]
    # attend(list)에서 반복
    for j in attend:
        # 모든 학생 list에서 출석한 학생요소는 제거
        every.remove(j)
    # 공백을 기준으로 every(list)를 합쳐서 반환
    return ' '.join(every)
```

```python
print(check(7, '1 3 5'))
>>
2 4 6 7
```



___

