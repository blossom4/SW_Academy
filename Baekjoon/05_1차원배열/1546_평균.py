# 1546

N = int(input())
score = list(map(int, input().split()))
max_score = 0
# 입력받은 점수들중 최고점수를 max_score에 저장
for i in range(N):
    if max_score < score[i]:
        max_score = score[i]
total = 0
# 조건에 주어진대로 점수를 최고점수로 나누고 100을 곱한다.
for i in range(N):
    total += (score[i] / max_score) * 100
avg = total / N
print(avg)