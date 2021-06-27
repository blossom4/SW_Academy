# SWEA 2050

A = str(input())
word_list = []
# 입력받은 문자를 아스키코드로 변환하여 계산하고, 다시 문자로 바꾸어준다.
for i in range(len(A)):
    word_list += [str(ord(A[i]) - 64)]
res = str.join(' ', word_list)
print(res)