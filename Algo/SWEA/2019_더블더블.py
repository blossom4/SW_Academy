# SWEA 2019

N = int(input())
N_list = []
num = 1
# 1 ~ N까지 반복
for i in range(N + 1):
    # index에 2를 곱해서 str형태로 리스트에 저장
    N_list += [str(num)]
    num *= 2
# 리스트에 저장된 값들을 공백으로 나눠서 res에 저장
res = str.join(' ', N_list)
print(res)