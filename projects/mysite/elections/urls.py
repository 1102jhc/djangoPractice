from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$',views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$',views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates)
    # url(r'^areas/(?P<area>\d)/$',views.areas) --숫자만 허용
]