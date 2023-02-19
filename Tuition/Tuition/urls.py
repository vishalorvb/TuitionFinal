
from django.contrib import admin
from django.urls import path
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')), 
    path(r'usermanager',include('usermanager.urls')), 
    path(r'tuition',include('Tuitionmanager.urls')), 
    path(r'teacher/',include('Teacher.urls')),
    path(r'payment/',include('payment.urls')),

]
