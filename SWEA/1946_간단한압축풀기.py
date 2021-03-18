# SWEA 1946

def arranging(arr):
    doc = ''
    a_doc = ''
    for i in range(len(arr)):
        doc += arr[i][0] * int(arr[i][1])

    while len(doc) > 0:
        if len(doc) >= 10:
            a_doc += doc[:10]
            a_doc += '\n'
            doc = doc[10:]
        else:
            a_doc += doc
            doc = []
            a_doc += '\n'
    return a_doc[:-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(str, input().split())))
    res = arranging(arr)
    print('#{}\n{}'.format(tc, res))