# 2577

A = int(input())
B = int(input())
C = int(input())
res = A * B * C
n_list = [0] * 10
# A,B,C를 곱한 숫자의 길이만큼 반복
for i in range(len(str(res))):
    # res에서 해당자리 숫자 번째의 index를 n_list에서 1씩 더한다.
    n_list[int(str(res)[i])] += 1
for i in range(10):
    print(n_list[i])