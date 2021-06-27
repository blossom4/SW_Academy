# SWEA 2007

T = int(input())
for tc in range(1, T+1):
    data = input()
    result = ''
 
    for i in range(1, len(data)):
        if data[0] == data[i] and data[0:i] == data[i:i*2]:
            result = data[0:i]
            break
 
    print("#{} {}".format(tc, len(result)))