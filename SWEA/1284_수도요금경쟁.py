# SWEA 1284

def water_bill(arr):
    p = arr[0]
    q = arr[1]
    r = arr[2]
    s = arr[3]
    w = arr[4]
    a_cost = p * w
    if r >= w:
        b_cost = q
    else:
        b_cost = q + (w - r) * s
    if a_cost > b_cost:
        return b_cost
    elif a_cost < b_cost:
        return a_cost

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    res = water_bill(arr)
    print('#{} {}'.format(tc, res))