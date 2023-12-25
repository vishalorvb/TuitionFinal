from django.urls import include, path,re_path
from Teacher import views


app_name = 'teacher'
urlpatterns = [
   
    re_path('teacher_page1', views.teacher_page1, name='teacher_page1'),
    re_path('teacher_page2', views.teacher_page2, name='teacher_page2'),
    re_path('create_teacher', views.create_teacher, name='create_teacher'),
    re_path('view_teacher', views.view_teacher, name='view_teacher'),
    re_path('unlock_teacher', views.unlock_teacher, name='unlock_teacher'),
    re_path('teacher_profile', views.Teacher_Profile, name='teacher_profile'),



    re_path('unlock_teacher', views.unlock_teacher, name='unlock_teacher'),
    re_path('create_teacher', views.create_teacher, name='create_teacher'),
    re_path('update_teacher_profile', views.update_teacher_Profile, name='update_teacher_profile'),
    re_path('getTecher_info', views.getTecher_info, name='getTecher_info'),
]

