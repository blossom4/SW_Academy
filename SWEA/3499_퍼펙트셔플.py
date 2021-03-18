# SWEA 3499

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    deck_1 = card[:(len(card) + 1) // 2]
    deck_2 = card[(len(card) + 1) // 2:]
    perfect = []
    for i in range(len(card)):
        if i % 2 == 0:
            perfect.append(deck_1[(i + 1) // 2])
        else:
            perfect.append(deck_2[i // 2])
    res = str.join(' ', perfect)
    print('#{} {}'.format(tc, res))