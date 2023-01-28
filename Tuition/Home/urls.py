from django.urls import include, path,re_path
from Home import views
app_name = 'Home'
urlpatterns=[
    re_path(r'^$',views.Home,name='Home'), 
    re_path(r'^error',views.error,name='error'), 
]