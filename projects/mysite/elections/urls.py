from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$',views.areas)
    # url(r'^areas/(?P<area>\d)/$',views.areas) --숫자만 허용
]