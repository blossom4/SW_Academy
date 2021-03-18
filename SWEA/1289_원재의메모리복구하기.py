# SWEA 1289

T = int(input())
for tc in range(1, T + 1):
    S = input()
    memory = []
    cnt = 0
    # 현재 index로부터 뒤에가 어떤값으로 쭉 설정되어있는지를 표지해주는 flag이다.
    flag = 0
    # 입력받은 문자열을 리스트 형태로 저장
    for i in range(len(S)):
        memory.append(S[i])
    for i in range(len(memory)):
        # memory 리스트를 검사하는데, 1을 처음 만나면 한번 바꿔주어야하므로,
        # cnt +1 해주고, 그 뒤는 모두 1로 변경되므로 flag = 1
        if memory[i] == '1' and flag == 0:
            cnt += 1
            flag = 1
        # 현재 메모리 정보가 0 인데 뒤는 1로 되어있을경우만
        # 만약 현재도  0이고 뒤에모든 메모리가 0이라면 굳이 건드릴 이유가 없기 때문이다.
        elif memory[i] == '0' and flag == 1:
            cnt += 1
            flag = 0
    print('#{} {}'.format(tc, cnt))