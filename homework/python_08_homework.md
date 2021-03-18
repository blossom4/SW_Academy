# python_08_homework



## 1. Circle 인스턴스 만들기

> **아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x, y좌표가 (2, 4)인 Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.**



___

## 2. Dog과 Bird는 Animal이다

> **다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.**

```python
class Animal():
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다.')
    
    def eat(self):
        print(f'{self.name}! 먹는다.')
# 상속받는 부분
class Dog(Animal):
    def bark(self):
        print(f'{self.name}! 짖는다.')
class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드득.')
```

```python
dog = Dog('멍멍이')
dog.walk()
dog.bark()
bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
>>
멍멍이! 걷는다.
멍멍이! 짖는다.
구구! 걷는다.
구구! 먹는다.
구구! 푸드득.
```



___

## 3. 오류의 종류

> **아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.**

- ZeroDivisionError

  0으로 나누려고 할때

- NameError

  없는 변수를 부르거나 함수를 사용하려할때

- TypeError

  실행하려고하는 명령의 타입이 맞지 않을때

- IndexError

  실행 불가능한 index범위를 지정해주었을때

- KeyError

  dict에서 없는 key이름을 불렀을때

- ModuleNotFoundError

  모듈이름을 정확히 부르지 않았을때

- ImportError

  모듈내에 특정 기능만 불러오려고했을때 그 기능 이름이 존재하지 않는경우



___

