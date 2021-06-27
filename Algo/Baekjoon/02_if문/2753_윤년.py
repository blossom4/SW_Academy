# 2753

# int형 input을 받는다.
year = int(input())
# 1. 400으로 나누어 떨어진다. True
# 2. 400으로 나누어 떨어지지 않고, 100으로 나누어 떨어진다. False
# 3. 400으로 나누어 떨어지지 않고, 100으로 나누어 떨어지지 않고, 4로는 나누어 떨어진다. True
# 4. 그 외는 모두 False
if year % 400 == 0:
    print(int(True))
elif year % 100 == 0:
    print(int(False))
elif year % 4 == 0:
    print(int(True))
else:
    print(int(False))