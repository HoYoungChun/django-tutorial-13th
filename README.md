# 과제내용정리 & 알게된 내용
## Part1

```python
django-admin startproject mysite # 현재 dir에 mysite라는 프로젝트생성(wrapping폴더명 바꿔도 상관없다)
python manage.py startapp polls # polls라는 앱 생성(바로 settings.py에 INSTALLED_APPS에 추가)
python manage.py runserver # 서버 실행(127.0.0.1:8000 또는 localhost:8000으로 접속)
```
프로젝트 이름으로 mysite.urls와 같이 프로젝트 어디서나 import 가능<br>
다른 port를 이용하고 싶으면 python manage.py runserver 8080과 같이 작성
