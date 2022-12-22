from django.urls import include, path,re_path
from Home import views
# from django.conf.urls import url
app_name = 'Home'
urlpatterns=[
    re_path(r'^$',views.Home,name='Home'), 
]