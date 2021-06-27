# 10951

# 무한루프
while 1:
    # 정상적으로 입력이 들어오면 결과출력
    try:
        A, B = map(int, input().split())
    # 입력이 정상적이지 않으면 break
    except:
        break
    print(A + B)