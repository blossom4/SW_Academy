# 2562

# 리스트 n_list에 숫자 9개를 입력받는다.
n_list = []
for i in range(9):
    n_list += [int(input())]
# 리스트를 돌면서 최대값을 max_num에 저장하고 그 때의 index를 따로
max_num = 0
index = -1
for i in range(9):
    if n_list[i] > max_num:
        max_num = n_list[i]
        index = i
print(max_num)
print(index + 1)