# 3052

n_list = []
# 숫자 10개를 입력받으면서 42로 나눈 나머지를 리스트에 더한다.
for i in range(10):
    N = int(input())
    n_list += [(N % 42)]
# set으로 중복되는 요소들을 모두 없애고 set의 길이를 출력한다.
print(len(set(n_list)))