# django_12_homework





## 1. 1:N True or False

1) T

2) F _set으로 전체데이터를 가져온 후 필요한 데이터를 뽑는다.

3) T

4) F



## 2. ForeignKey column name

컬럼의 이름: answer_id

테이블의 이름: articles_comment



## 3. 1:N model manager

(a): question.comment_set.all



## 4. next parameter

1) @login_required (삭제)

if request.user.is_authenticated: (이렇게 사용)

이유:  로그인이 실패할경우 다시 GET방식으로 요청이 가게되는데 이때 POST방식이아니므로 조건문을 통과할 수 없다.