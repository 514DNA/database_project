from django.conf.urls import url
from django.contrib import admin
from user_system import views
 
urlpatterns = [
    url(r'^$', views.test_views,name='test_views'),
    url(r'^admin/', admin.site.urls),
]