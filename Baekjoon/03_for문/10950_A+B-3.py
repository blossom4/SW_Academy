# 10950

# int형 input을 받는다.
t = int(input())
input_list = []
# 0~2t까지 2씩 증가하면서 반복
for i in range(0, t * 2, 2):
    # ' '을 잘라낸 여러가지 input 정보를 int형으로 받는다.
    a, b = map(int, input().split(' '))
    # input받은 정보를 input_list(list)에 더한다.
    input_list.insert(i, a)
    input_list.insert(i + 1, b)
# 0~2t까지 2씩 증가하면서 반복
for j in range(0, t * 2, 2):
    # input_list(list)의 요소를 두개씩 더하면서 출력
    res = input_list[j] + input_list[j + 1]
    print(res)