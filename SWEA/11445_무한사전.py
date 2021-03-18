# SWEA 11445

T = int(input())
for tc in range(1, T + 1):
    P = str.join('', input().split())
    Q = str.join('', input().split())
    P += 'a'
    if P == Q:
        print('#{} N'.format(tc))
    else:
        print('#{} Y'.format(tc))