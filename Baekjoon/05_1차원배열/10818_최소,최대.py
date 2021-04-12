# 10818

# 최소값 얻는 함수
def get_min(n_list):
    min_num = 1000000
    for i in range(len(n_list)):
        if n_list[i] < min_num:
            min_num = n_list[i]
    return min_num

# 최대값 얻는 함수
def get_max(n_list):
    max_num = -1000000
    for i in range(len(n_list)):
        if n_list[i] > max_num:
            max_num = n_list[i]
    return max_num

N = int(input())
n_list = list(map(int, input().split()))
print('{} {}'.format(get_min(n_list), get_max(n_list)))