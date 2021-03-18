# SWEA 4875

def calculate(arr):
    stk = []
    for i in forth:
        if i == '.':
            if len(stk) == 1:
                return int(stk.pop())
            else:
                break
        elif i == '+' or i == '-' or i == '/' or i == '*':
            if len(stk) >= 2:
                b = int(stk.pop())
                a = int(stk.pop())
                if i == '+':
                    stk.append(a + b)
                elif i == '-':
                    stk.append(a - b)
                elif i == '/':
                    stk.append(a / b)
                elif i == '*':
                    stk.append(a * b)
            else:
                break
        else:
            stk.append(i)
    return 'error'

T = int(input())
for tc in range(1, T + 1):
    forth = input().split()
    answer = calculate(forth)
    print(f'#{tc} {answer}')