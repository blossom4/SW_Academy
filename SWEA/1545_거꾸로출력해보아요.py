# SWEA 1545

N = int(input())
N_list = []
# N + 1만큼 반복
for i in range(N + 1):
    # N에서 index를 뺀 수를 str형태로 리스트에 저장
    N_list += [str(N - i)]
# 공백을 기준으로 나눠서 리스트를 합쳐진 문자열로 나타내 res에 저장
res = str.join(' ', N_list)
print(res)