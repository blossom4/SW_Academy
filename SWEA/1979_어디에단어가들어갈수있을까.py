# SWEA 1979

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    area = []
    for i in range(N):
        N_list = list(map(int, input().split()))
        area.append(N_list)
    length = 0
    cnt = 0
    # 가로찾기
    for i in range(N):
        for j in range(N):
            # 1이 나올경우 1을 따라가다가 j가 끝까지가면,
            # length가 K와 같은지 비교. 같으면 cnt += 1, length 초기화
            if area[i][j] == 1:
                length += 1
                if j == N - 1:
                    if length == K:
                        cnt += 1
                    length = 0
            # 1을 따라가다가 1외의 다른것 0을 만나면 length를 K와 비교.
            # 같으면 cnt += 1, length 초기화
            else:
                if length == K:
                    cnt += 1
                length = 0
                
    # 세로찾기 (가로와 마찬가지 원리)
    for i in range(N):
        for j in range(N):
            if area[j][i] == 1:
                length += 1
                if j == N - 1:
                    if length == K:
                        cnt += 1
                    length = 0
            else:
                if length == K:
                    cnt += 1
                length = 0
 
    print('#{} {}'.format(tc, cnt)) 