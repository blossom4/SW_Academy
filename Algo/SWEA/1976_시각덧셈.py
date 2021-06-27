# SWEA 1976

def get_time(arr):
    time_sum = [0, 0]
    time_sum[0] += arr[0] + arr[2]

    # 분 검사
    if arr[1] + arr[3] >= 60:
        time_sum[0] += 1
        time_sum[1] += arr[1] + arr[3] - 60
    else:
        time_sum[1] += arr[1] + arr[3]

    # 시 검사
    if time_sum[0] >= 12:
        time_sum[0] -= 12

    # 리스트를 문자열로 변환
    for i in range(2):
        time_sum[i] = str(time_sum[i])
    res = str.join(' ', time_sum)
    return res

T = int(input())
for tc in range(1, T + 1):
    time_list = list(map(int, input().split()))
    res = get_time(time_list)
    print('#{} {}'.format(tc, res))