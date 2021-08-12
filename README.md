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

##2021. 08. 11
```
여론 조사 화면 구현
```

##2021. 08. 12
```
여론 조사 저장
```
