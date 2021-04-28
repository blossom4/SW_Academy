# django_17_homework



## 1.

- JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다.  (F)
- DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다. (F) 
  - postman
-  api_view 데코데이터를 사용하지 않아도 HTTP Method에 대한 요청에 응답할 수 있다. (F)
  - django에서는 필수이다.
-  Serializers는 Queryset 객체를 JSON 포맷으로 변환 할 수 있는 python 데이터 타입으로 만 들어준다. (T)
  - Queryset 객체 -> python 데이터타입 -> JSON 포맷



## 2.





## 3.

(a) POST

(b) data=request.data

(c) raise_exception=True

(d) serializer.data

(e) status=200