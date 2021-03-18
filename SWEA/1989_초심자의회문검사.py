# SWEA 1989

def examine_palindrome(S):
    for i in range((len(S) - 1) // 2):
        if S[i] != S[len(S) - i - 1]:
            return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    S = input()
    res = examine_palindrome(S)

    print('#{} {}'.format(tc, res))