# SWEA 1974

def examine_sdoku(arr):
    
    # 가로줄 검사
    for i in range(9):
        line_x = []
        for j in range(9):
            line_x.append(arr[i][j])
        # 가로줄의 숫자를 리스트에 넣고 set해서 중복되어있으면,
        # 중복된 요소가 제거되므로, 길이가 9보다 작아짐
        if len(set(line_x)) != 9:
            return 0
            
    # 세로줄 검사
    for j in range(9):
        line_y = []
        for i in range(9):
            line_y.append(arr[i][j])
        # 세로줄의 숫자를 리스트에 넣고 set해서 중복되어있으면,
        # 중복된 요소가 제거되므로, 길이가 9보다 작아짐
        if len(set(line_y)) != 9:
            return 0
    
    # 칸 검사
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            box = []
            for k in range(3):
                for l in range(3):
                    box.append(arr[i + k][j + l])
        if len(set(box)) != 9:
            return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = examine_sdoku(arr)
    print('#{} {}'.format(tc, res))