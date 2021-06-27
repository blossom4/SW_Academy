# SWEA 1933

N = int(input())
divisor_list = []
# 1 ~ N 까지 반복
for i in range(1, N + 1):
    # index로 나누어 떨어지면 divisor_list에 추가
    if N % i == 0:
        divisor_list += [str(i)]
# divisor_list의 요소들 사이에 공백을 넣어서 str형태로 res에 저장
res = str.join(' ', divisor_list)
print(res)