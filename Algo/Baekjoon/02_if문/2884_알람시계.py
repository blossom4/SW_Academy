# 2884

# ' '을 잘라낸 여러가지 input 정보를 int형으로 받는다.
h, m = map(int, input().split(' '))
# 1. 45분 이후이면 시간(h)는 그대로, 분(m) -45
# 2. 시간이 1시 이후이고, 45분 이전이면 시간은 h-1, 분은 60-(45-m)
# 3. 시간이 0시 이고, 45분 이전이면 시간은 23, 분은 60-(45-m)
if m >= 45:
    print('{} {}'.format(h, m - 45))
elif h > 0 and m < 45:
    print('{} {}'.format(h - 1, 60 - (45 - m)))
elif h == 0 and m < 45:
    print('23 {}'.format(60 - (45 - m)))