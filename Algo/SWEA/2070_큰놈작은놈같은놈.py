# SWEA 2070

def distinction(a, b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '='

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc, distinction(a, b)))