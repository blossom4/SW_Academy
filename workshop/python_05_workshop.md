# python_05_workshop

> Data Structure
>
> Method



## 1. 평균 점수 구하기

> key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 `get_dict_avg` 함수를 작성하시오.



```python
def get_dict_avg(scores):
    total = []
    # scores(dict)만큼 반복
    for i in range(len(scores)):
        # value 값들을 꺼내서 total에 더한다.
        total += scores.values()
        # 평균 = 총합 / 개수
        avg = sum(total) / len(scores)
        return avg
```

```python
scores_a = {
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
}
print(get_dict_avg(scores_a))
>>
85.5
```



___

## 2. 혈액형 분류하기

> 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.



```python
def count_blood(bld):
    total = []
    bld_dict = {}
    cnt_a, cnt_b, cnt_ab, cnt_o = 0, 0, 0, 0
    # input 받은 dict의 길이만큼 반복
    for i in range(len(bld)):
        # 각각의 혈액형을 만날때마다 cnt +1
        if bld[i] == 'A':
            cnt_a += 1
        elif bld[i] == 'B':
            cnt_b += 1
        elif bld[i] == 'AB':
            cnt_ab += 1
        else:
            cnt_o += 1
    # 각각의 '혈액형'을 key로, 'cnt'를 value로 갖는 dict를 만든다.
    bld_dict['A'] = cnt_a
    bld_dict['B'] = cnt_b
    bld_dict['AB'] = cnt_ab
    bld_dict['O'] = cnt_o
    return bld_dict
```

```python
cnt_list = [
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]
print(count_blood(cnt_list))
>>
{'A': 3, 'B': 3, 'AB': 3, 'O': 3}
```

