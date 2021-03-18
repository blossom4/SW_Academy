# SWEA 1926

N = int(input())
arr_369 = []
for i in range(1, N + 1):
    # 숫자에 3 6 9중 하나가 있다면,
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0
        # 숫자의 길이만큼 반복하면서 369가 있을때마다(박수를 쳐야하는 횟수) cnt +1
        for j in range(len(str(i))):
            if str(i)[j] == '3' or str(i)[j] == '6' or str(i)[j] == '9':
                cnt += 1
        # 박수를 쳐야하는 횟수 cnt 만큼 '-'를 리스트에 추가한다.
        arr_369.append('-' * cnt)
        continue
    # 숫자에 3 6 9중 하나도 없다면 그대로 리스트에 추가
    arr_369.append(str(i))

print(*arr_369)