# python_07_workshop



## 1. pip

> **아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성 하시오.**

```python
$ pip install faker
```

(1) 샘플 데이터 생성기이다.

(2) 명령어로 입력해주면 된다.



___

## 2. Basic Usages

> **Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다. **
>
> **임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.**

```python
# (1) faker 모듈에서 샘플랜덤데이터를 생성하는 기능을 가져온다.
from faker import Faker
# (2) fake를 Faker 기능을 사용하는 명령어로 지정한다.
fake = Faker()
# (3) 이름샘플을 랜덤하게 생성한다.
fake.name()
```



___

## 3. Localization

> **Faker는 다양한 언어의 Locale을 지원한다.**

1. 인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)

   ```python
   fake = Faker()
   fake.name()
   >>
   # 랜덤한 영문이름 샘플데이터가 출력된다.
   ```

2. Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.

   ```python
   fake_ko = Faker('ko_KR')
   fake_ko.name()
   >>
   # 랜덤한 한글이름 샘플데이터가 출력된다.
   ```

   

>  **직접 해당하는 기능을 구현한다고 하였을 때,  코드로 적절한 것을 작성하시오.**

```python
class Faker():
    
    def __init__(self, locale = 'en_US')
```



___

