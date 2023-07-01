from django.urls import include, path,re_path
from usermanager import views
from django.conf.urls.static import static  
from django.conf import settings  

app_name = 'usermanager'
urlpatterns=[
    re_path(r'^/registration$',views.registration,name='registration'),
    re_path(r'^/login$',views.login_page, name='login_page'),
    re_path(r'^/verify_otp$',views.verify_otp,name='verify_otp'),
    re_path(r'^/logout',views.user_logout,name='logout'),
   
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  