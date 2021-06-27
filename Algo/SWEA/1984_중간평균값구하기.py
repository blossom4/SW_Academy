# SWEA 1984

def middle_avg(arr):

    # 입력받은 10개의 숫자리스트를 오름차순으로 정렬
    for i in range(10):
        for j in range(9):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    total_sum = 0
    # 최소값인 0번째 요소와 최대값인 9번째 요소를 제외하고 합산
    for i in range(1, 9):
        total_sum += arr[i]
    
    return round(total_sum / 8)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    res = middle_avg(arr)

    print('#{} {}'.format(tc, res))