# SWEA 11315

def examine_five(arr, N):
    yes = 'YES'
    no = 'NO'
    # 세로 검사
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 'o':
                # 오목돌을 만났지만 애초에 남은 칸수가 5칸이 안되면 더이상 검사할 필요가 없다.
                if N - i < 5:
                    continue
                else:
                    for k in range(5):
                        # 오목돌 5개가 들어갈 칸은 남아있지만 오목돌(cnt)이 5개가 되기전에,
                        # 다음 검사방향에서 '.'을 만나면 더이상 검사할 필요가 없다.
                        if arr[i + k][j] == '.':
                            break
                        else:
                            cnt += 1
                    if cnt == 5:
                        return yes
    # 가로 검사
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 'o':
                # 오목돌을 만났지만 애초에 남은 칸수가 5칸이 안되면 더이상 검사할 필요가 없다.
                if N - j < 5:
                    continue
                else:
                    for k in range(5):
                        # 오목돌 5개가 들어갈 칸은 남아있지만 오목돌(cnt)이 5개가 되기전에,
                        # 다음 검사방향에서 '.'을 만나면 더이상 검사할 필요가 없다.
                        if arr[i][j + k] == '.':
                            break
                        else:
                            cnt += 1
                    if cnt == 5:
                        return yes
    # 대각선1 검사
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 'o':
                # 오목돌을 만났지만 애초에 남은 칸수가 5칸이 안되면 더이상 검사할 필요가 없다.
                if N - i < 5 or N - j < 5:
                    continue
                else:
                    for k in range(5):
                        # 오목돌 5개가 들어갈 칸은 남아있지만 오목돌(cnt)이 5개가 되기전에,
                        # 다음 검사방향에서 '.'을 만나면 더이상 검사할 필요가 없다.
                        if arr[i + k][j + k] == '.':
                            break
                        else:
                            cnt += 1
                    if cnt == 5:
                        return yes
    # 대각선2 검사
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 'o':
                # 오목돌을 만났지만 애초에 남은 칸수가 5칸이 안되면 더이상 검사할 필요가 없다.
                if N - i < 5 or j < 4:
                    continue
                else:
                    for k in range(5):
                        # 오목돌 5개가 들어갈 칸은 남아있지만 오목돌(cnt)이 5개가 되기전에,
                        # 다음 검사방향에서 '.'을 만나면 더이상 검사할 필요가 없다.
                        if arr [i + k][j - k] == '.':
                            break
                        else:
                            cnt += 1
                    if cnt == 5:
                        return yes
    return no

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, examine_five(arr, N)))