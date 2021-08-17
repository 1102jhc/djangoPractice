# djangoPractice
장고 연습

**MVC MODEL**
```
MODEL(데이터) - models.py
- 정의된 클래스의 형식대로 데이터를 DB에 저장 or 불러오기

View(화면) - templates
- 화면에 어떤 장면을 보여줄지 정의

Controller(조율) - views.py
- 정의된 모델에서 데이터를 읽어, view에 전달

```
*****

**MVC Flow**
``` 
    mysite - urls.py 
->  elections - urls.py 
->  views.py (Models.py 참조)
->  templates - *.html
```

*****

#Trouble Shooting
```
1. django는 debug = true 로 하는 것은 권장하지 않는다. 
하여 false로 설정하면 admin 페이지에 css가 미적용 된다.

해결법)
urls.py>
from django.views.static import serve
url(r'^static/(?P<path>.*)', serve, kwargs={'insecure': True})  # urlpatterns에 추가

settings.py>
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # STATIC_URL 밑에 추가

python manage.py collectstatic # static files를 모아준다.

python manage.py runserver --insecure # 서버 실행

```
##2021. 08. 11
```
여론 조사 화면 구현
```

##2021. 08. 12
```
여론 조사 저장
여론 조사 결과 보기
```

