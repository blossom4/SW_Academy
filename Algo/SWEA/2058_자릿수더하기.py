# SWEA 2058

N = int(input())
total_sum = 0
while N > 0:
    total_sum += N % 10
    N //= 10
print(total_sum)