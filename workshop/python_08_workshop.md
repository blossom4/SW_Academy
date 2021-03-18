# python_08_workshop



## 1. 도형 만들기

> **아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하시오.**



**Point 클래스에 대한 명세는 다음과 같다.**

- 인스턴스변수 = x / Type = int / x 좌표
- 인스턴스변수 = y /Type = int / y 좌표
- method = 생성자 / 매개변수 x 좌표, y좌표 / return값 = 없음

**Rectangle 클래스에 대한 명세는 다음과 같다.**

- 인스턴스변수 = p1 / Type = Point 인스턴스 / 좌측 상단 좌표
- 인스턴스변수 = p2 / Type = Point 인스턴스 / 우측 하단 좌표
- method = 생성자 / 매개변수 point 인스턴스 / return값 = 없음
- method = get_area / 매개변수 없음 / return값 = 넓이(int)
- method = get_perimeter / 매개변수 없음 / return값 = 둘레 길이(int)
- method = is_square / 매개변수 없음 / 정사각형 판별(bool)

```python
class Point():
    # Point라는 class에서 x값과 y값을 저장한다.
    def __init__(self, x, y):        
        self.x = x
        self.y = y
                
class Rectangle():
    # Rectangle class에서 p1값과 p2값을 저장한다.
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
	# .p1.x, .p1.y, .p2.x, .p2.y 와 같은 방법으로 다른 클래스의 값을 불러올 수 있다.
    def get_area(self):
        # 사각형의 넓이
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
    
    def perimeter(self):
        # 사각형의 둘레
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2
    
    def is_square(self):
        # 가로와 세로의 길이가 같으면 정사각형이므로 True반환
        if self.p2.x - self.p1.x == self.p1.y - self.p2.y:
            return True
        # 다르면 False 반환
        else:
            return False
```

```python
p1 = Point(1, 3)
p2 = Point(3, 1)
r = Rectangle(p1, p2)
```

```python
r.get_area()
>>
4
```

```python
r.perimeter()
>>
8
```

```python
is_square
>>
True
```



___

