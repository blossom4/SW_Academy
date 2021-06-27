# python_04_workshop

> Function



## 1. 숫자의 의미

> 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. (단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.)



```python
def get_secret_word(numbers):
    # numbers(list)에서 반복
    for i in range(len(numbers)):
        # chr() 함수로 정수를 해당되는 문자로 변환
        print(chr(numbers[i]), end = '')
get_secret_word([75, 97, 107, 97, 111, 70, 114, 105, 101, 110, 100, 115])
>>
KakaoFriends
```



___

## 2. 내 이름은 몇일까?

> 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.



```python
def get_secret_number(name):
    res = 0
    # name(string)에서 반복
    for i in range(len(name)):
        # ord() 함수로 문자를 해당되는 정수로 변환해서 더한다.
        res += ord(name[i])
    print(res)
get_secret_number('Ryan')
>>
410
```



___

## 3. 강한 이름

> 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.



```python
# 2.내 이름은 몇일까? 의 함수 활용
def get_secret_number(name):
    res = 0
    for i in range(len(name)):
        res += ord(name[i])
    return res

def get_strong_word(str1, str2):
    a = get_secret_number(str1)
    b = get_secret_number(str2)
    # 문자열을 정수로 변환하고 비교한다.
    if a > b:
        print(str1)
    else:
        print(str2)
get_strong_word('z', 'a')
get_strong_word('tom', 'john')
>>
z
john
```



___

