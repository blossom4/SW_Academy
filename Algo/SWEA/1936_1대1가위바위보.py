# SWEA 1936

A, B = map(int, input().split())
# A가 이기는 경우 3가지를 조건에 걸고 만족하면 A 출력
if (A == 1 and B == 3) or (A == 2 and B ==1) or (A == 3 and B == 2):
    print('A')
# 그렇지 않을 경우 B 출력
else:
    print('B')