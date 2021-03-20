# 과제내용정리 & 알게된 내용
## Part1

```python
# 현재 dir에 mysite라는 프로젝트생성(wrapping폴더명 바꿔도 상관없다)
django-admin startproject mysite
# polls라는 앱 생성(바로 settings.py에 INSTALLED_APPS에 추가)
python manage.py startapp polls
# 서버 실행(127.0.0.1:8000 또는 localhost:8000으로 접속)
python manage.py runserver
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


## part2
SQLite 를 데이터베이스로 사용하지 않는 경우, USER, PASSWORD, HOST 같은 추가 설정이 반드시 필요합니다.
```python
# 마이그레이션 파일 생성
python manage.py makemigrations <app-name>
# 마이그레이션 적용
python manage.py migrate <app-name>
```
데이터베이스의 각 필드는 Field 클래스의 인스턴스로서 표현됩니다.<br>
몇몇 Field 클래스들은 필수 인수가 필요합니다. 예를 들어, CharField 의 경우 max_length 를 입력해 주어야 합니다. 또한 Field 는 다양한 선택적 인수들을 가질 수 있습니다.<br>
 sqlmigrate 명령은 migration 이름을 인수로 받아, 실행하는 SQL 문장을 보여줍니다.
```python
# Python 쉘 실행
python manage.py shell
```
단순히 "python" 이라고 실행하는 대신에 위의 명령을 실행한 까닭은, manage.py 에 설정된 DJANGO_SETTINGS_MODULE 환경변수 때문입니다.<br>
이 환경변수는 mysite/settings.py 파일에 대한 Python 임포트 경로를 Django에게 제공합니다.

```python
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```
모델에 __str__() 메소드를 추가하는것은 객체의 표현을 대화식 프롬프트에서 편하게 보려는 이유 말고도,
Django가 자동으로 생성하는 관리 사이트 에서도 객체의 표현이 사용되기 때문입니다.
```python
Question.objects.all() #Question Object 모두 가져오기
Question.objects.filter(id=1) #id가 1인 Question Object 가져오기
Question.objects.filter(question_text__startswith='What') # __로 lookup적용(https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id4)
q.was_published_recently() #모델에 있는 커스텀 메소드 실행
q.choice_set.all() #해당 Question 객체를 foreign key로 참조하는 모든 Choice 객체를 가져온다
q.choice_set.create(choice_text='Not much', votes=0) #해당 Question 객체를 foreign key로 참조하는 Choice 객체 생성
Choice.objects.filter(question__pub_date__year=current_year) #__로 Foreign key의 Field접근
```
관련 객체에 접근하기: <https://docs.djangoproject.com/ko/3.0/ref/models/relations/> <br>
필드 조회(lookup): <https://docs.djangoproject.com/ko/3.0/topics/db/queries/#field-lookups-intro> <br>
데이터베이스 API 레퍼런스: <https://docs.djangoproject.com/ko/3.0/topics/db/queries/> <br>
```python
# 관리자 생성, http://127.0.0.1:8000/admin/으로 접근
python manage.py createsuperuser
```
관리 사이트에서 poll app 변경가능하도록 admin.py에 작성
```python
from django.contrib import admin
from .models import Question
admin.site.register(Question)
```
