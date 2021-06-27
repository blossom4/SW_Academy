# django_02_homework



## 1. MTV

> Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.



MVC모델 (Model - View - Controller)

MTV모델 (Model - Templates - View)

각각 DB설계, 관리 - HTML로 보여지는부분 - 데이터 받고 전달 하는 역할을 한다.



___

## 2. URL

> __(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇인지 작성하시오.



(a) : 라우팅



___

## 3. Django template path

> Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.



(a) : templates



___

## 4. Static web and Dynamic web

> Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.



Static web page : 

- 서버(web server)에 ***'미리저장된 파일'(html , css , js ,video  image 등)을 그대로를 클라이언트에게 응답***한다.
- 서버는 사용자의 요청(request)에 해당되는 ***'저장된 웹페이지'를 응답해준다.(response)***

- 사용자가 서버에 저장된 데이터를 ***'변경하지 않는 한'*** 고정된 웹페이지를 보게된다. 



Dynamic web page :

- 서버(웹서버)에 있는 데이터들을 스크립트에 의해 '**가공처리한 후 생성' 되어 전달**

- "서버"는 사용자의 request를 해석하여 데이터를 **'가공후' 생성되는 웹페이지 보냄**

●- **사용자는 상황 , 시간 , 요청 등에 따라 달라지는 웹페이지** 



___

