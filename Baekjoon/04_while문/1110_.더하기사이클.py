# 1110

def plus_cycle(n):
    # 주어진 수의 일의 자리숫자
    temp_1 = n % 10
    # 새롭게 더해진 숫자의 십의자리 와 일의자리의 합
    temp_2 = (n // 10) + (n % 10)
    # 새로운 수
    res = temp_1 * 10 + temp_2 % 10
    return res

N = int(input())
temp = N
cnt = 0
# 무한루프
while 1:
    # 입력받은 숫자 N이 주어진 문제의 조건대로 더하기 사이클을 한 수를 다시 N에 저장
    N = plus_cycle(N)
    # 한번 진행할때마다 cnt +1
    cnt += 1
    # temp에 저장해두었던 처음입력받는 숫자가 더하기사이클을 지나고 난 수와 같으면 break
    if N == temp:
        break
print(cnt)