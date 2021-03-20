# 과제내용정리 & 알게된 내용
## Part1

```python
django-admin startproject mysite # 현재 dir에 mysite라는 프로젝트생성(wrapping폴더명 바꿔도 상관없다)
python manage.py startapp polls # polls라는 앱 생성(바로 settings.py에 INSTALLED_APPS에 추가)
python manage.py runserver # 서버 실행(127.0.0.1:8000 또는 localhost:8000으로 접속)
```
프로젝트 이름으로 mysite.urls와 같이 프로젝트 어디서나 import 가능<br>
다른 port를 이용하고 싶으면 python manage.py runserver 8080과 같이 작성

### path()
path의 인수에는 route, view, kwargs, name이 있습니다.
* route<br>
    > route는 URL 패턴을 가진 문자열 입니다.<br>
    > 요청이 처리될 때, Django 는 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교합니다.<br>
    > 패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않습니다. 
* view<br>
    > Django 에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고,<br> 경로로 부터 '캡처된' 값을 키워드 인수로하여 특정한 view 함수를 호출합니다.
* kwargs
    > 임의의 키워드 인수들은 목표한 view 에 사전형으로 전달됩니다.
* name
    > URL에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다.

### include()
include() 함수는 다른 URLconf들을 참조할 수 있도록 도와줍니다.<br>
URL의 해당 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분은 include 된 URLconf로 전달합니다.<br>
admin.site.urls을 제외하고 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 합니다.