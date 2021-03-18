# SWEA 1859

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price_list = list(map(int, input().split()))
    start = 0
    profit = 0
    while len(price_list) > 0:
        cnt = 0
        buy = 0
        max_value = -1
        max_index = -1
        # 가격리스트의 길이만큼 반복하면서, 최대가격과 그 index를 저장한다.
        for i in range(len(price_list)):
            if max_value <= price_list[i]:
                max_value = price_list[i]
                max_index = i
        # 최대가격에 해당하는 index까지 모두다 매입해서(buy),
        # 최대 가격이 되는 때에 모두 판매(profit)한다.
        for i in range(max_index):
            cnt += 1
            buy += price_list[i]
        profit += price_list[max_index] * cnt - buy
        # 현재의 최대 index인 날까지 최대의 이윤을 보고 판매하였으므로,
        # 그 이후부터 똑같이 반복한다.(만약 최대가격이 맨 앞에 있다면 아무 계산도 하지않고 리스트에서 제거된다.)
        price_list = price_list[max_index + 1:]
    print('#{} {}'.format(tc, profit))