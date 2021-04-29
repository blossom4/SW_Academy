# 08_Module

> **파일 단위의 코드 재사용**

- 모듈(Module)
  - 특정 기능을 `.py` **파일 단위**로 작성한 것.
- 패키지(Package)
  - 파이썬에 **기본적으로 설치된 모듈과 내장 함수**를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 불림.



## 모듈(Module)

> **모듈(module)은 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)이다.**



module 생성

- module로 활용할 파일에 함수를 작성해 .py파일로 저장

module활용

- 모듈을 활용하기 위해서는 반드시 `import`문을 통해 내장 모듈을 이름 공간으로 가져와야한다.



## 패키지(Package)

> **패키지(pakcage)는 점(`.`)으로 구분된 모듈 이름(`package.module`) 을 써서 모듈을 구조화하는 방법이다.**



package 생성

- python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식한다(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것이 권장된다.

package 활용

- 모듈과 동일하게 `from`과 `import` 키워드를 통해 코드를 가져와(import) 활용한다.

  1. **from <package> import <module>**

  2. **from <package.module> import <data> **

     특정한 함수 혹은 어트리뷰트만 활용하고 싶을 때

  3. **from <module> import ***

     해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져온다.

  4. **from <module> import <data> as <name>**

     내가 지정하는 이름을 붙여 가져올 수 있다.