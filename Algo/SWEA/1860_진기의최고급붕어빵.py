# SWEA 1860

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    time = 0
    bun = 0
    # 손님이 오는 초를 리스트에 저장하고, 가장 늦게오는 손님을 기준으로,
    # 방문 리스트를 만든다.
    for i in range(N):
        if time < customer[i]:
            time = customer[i]
    comming = [0] * (time + 1)
    # 손님이 방문한 시간초에 해당하는 index를 방문리스트에 +1하여 체크한다.
    for i in range(N):
        comming[customer[i]] = 1
    # 만약 0초에 손님이 온다면 붕어빵을 줄 수 없으므로, 
    # Impossible을 저장하고 반복문을 빠져나온다.
    for i in range(1, time + 1):
        if comming[0] == 1:
            res = 'Impossible'
            break
        # M초마다 K개의 붕어빵을 더해준다.
        if i % M == 0:
            bun += K
        # 방문리스트에 손님이 있을경우 붕어빵 하나를 뺀다.
        if comming[i] == 1:
            bun -= 1
            # 그런데 만약 줄 붕어빵이 남아있지 않은경우 Impossible 저장후 반복문을 빠져나온다.
            if bun < 0:
                res = 'Impossible'
                break
        # 앞의 모든 조건을 끝까지 거쳤음에도 한번도 붕어빵의 개수가 음수로 내려가지 않았다면,
        # 가능한 경우이므로 Possible 을 res에 저장
        if i == time and bun >= 0:
            res = 'Possible'
    print('#{} {}'.format(tc, res))