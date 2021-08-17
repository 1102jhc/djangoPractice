from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url('', include('elections.urls')),
    url('admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)', serve, kwargs={'insecure': True})
]
