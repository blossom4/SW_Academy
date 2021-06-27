# 8958

T = int(input())
for tc in range(1, T + 1):
    res = input()
    total = 0
    get_score = 1
    for i in range(len(res)):
        # 정답이면 get_score 1점을 얻는다. 
        # 이때 이전문제도 정답이었으면 get_score 자체가 1더해진다.
        if res[i] == 'O':
            if res[i - 1] == 'O' and i != 0:
                get_score += 1
            total += get_score
        # 정답이 아닐경우 얻는점수 get_score은 1이된다.
        else:
            get_score = 1
    print(total)