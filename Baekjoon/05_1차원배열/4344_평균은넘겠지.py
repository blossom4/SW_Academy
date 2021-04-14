# 4344

T = int(input())
for tc in range(1, T + 1):
    score = list(map(int, input().split()))
    total = 0
    # 학생들의 평균 avg를 구한다.
    for i in range(1, score[0] + 1):
        total += score[i]
    avg = total / score[0]
    cnt = 0
    # 평균 avg보다 점수가 높은 학생수를 cnt
    for i in range(1, score[0] + 1):
        if score[i] > avg:
            cnt += 1
    # 소수점 넷째자리에서 반올림해서 세째자리까지 표현
    ratio = ('{:.03f}').format((cnt / score[0]) * 100)
    print('{}%'.format(ratio))