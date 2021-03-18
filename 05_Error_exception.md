# 05_Error_exception



## 에러(Error)



## 문법 에러(Syntax error)

문법 에러가 있는 프로그램은 실행되지 않는다.

- 에러 발생시 `SyntaxError`라는 키워드와 함께, 에러의 상세 내용을 보여준다.
- `파일이름`과 `줄번호`, `^`문자로 파이썬이 코드를 읽어 들일 때 (`parser`) 문제가 발생한 위치를 표현한다.
- `parser`은 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 작은 '화살표(`^`)'를 표시한다.



## 예외(Exception)

실팽 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춘다.

- 문법적으로는 옳지만, 실행시 발생하는 에러이다.



## 예외 처리(Exception Handling)

> **try / except**

`try` 문을 이용하여 예외 처리를 할 수 있다.

기초 문법

```python
try:
    <code block 1>
except (예외):
    <code block 2>
```

- `try` 아래의 코드블락(code block)이 실행된다.
- 예외가 발생되지 않으면, **`except`없이 실행이 종료 된다.**
- 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.