# SWEA 1983

def get_grade(arr, N, K):
    grade_gap = N // 10
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_list = []
    student_score = 0
    student_grade = 0

    # 입력받은 학생들의 최종점수를 계산해서 리스트에 저장
    for i in range(N):
        final_score = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2
        grade_list.append(final_score)
        # 현재 계산중인 점수가 내가 구해야하는 K번째 학생이라면 student_score에 점수를 따로저장
        if i == K - 1:
            student_score = final_score
        final_score = 0
    
    # grade_score에 저장한 점수리스트들을 버블배열로 내림차순 정렬
    for i in range(N):
        for j in range(N - 1):
            if grade_list[j] < grade_list[j + 1]:
                temp = grade_list[j]
                grade_list[j] = grade_list[j + 1]
                grade_list[j + 1] = temp
    
    # K번째 학생의 최종점수가 전체학생중 몇등(몇번째index)인지 구해서 student_grade에 저장
    for i in range(N):
        if student_score == grade_list[i]:
            student_grade = i
            break
    # '학생의 등수'를 '점수별로 줄수있는 학생 수(N // 10)로 나눈 몫'에 
    # 해당하는 grade의 index가 K번째 학생이 받아야하는 등급이다.
    res = grade[student_grade // (grade_gap)]

    return res


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = get_grade(arr, N, K)

    print('#{} {}'.format(tc, res))