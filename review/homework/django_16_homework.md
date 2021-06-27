# django_16_homework



## 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. (T)
- HTTP Method는 GET과 POST 두 종류가 있다.  (DELETE PUT 등등) (F)
- 일반적으로 URI 마지막에 슬래시( / )는 포함하지 않는다. (T) (django에서는 붙인다.)
- ‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현 한 RESTful한 URI라고 할 수 있다. (create와 같은 동사이름은 지양한다.) (F)



## 2.

200 요청성공

400 잘못되었다. (서버가 이해할 수 없다.)

401 미인증 (인증을 해야한다.)

403 csrf_token 접근권한이 없다.

404 나에게 없는 리소스이다.

500 서버 자체가 없다.



## 3.

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Student
        fields = '__all__'
```



## 4.

쿼리셋을 json으로 바꾸기 위해 사용한다.