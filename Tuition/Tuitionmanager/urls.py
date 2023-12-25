from django.urls import include, path,re_path
from Tuitionmanager import views
app_name = 'tuition'
urlpatterns = [
    re_path(r'^/post_tuition_page1$', views.post_tuition_page1, name='post_tuition_page1'),
    re_path(r'^/post_tuition_page2', views.post_tuition_page2, name='post_tuition_page2'),
    re_path(r'^/save_tuition', views.save_tuition, name='save_tuition'),
    re_path(r'^/tuitions$', views.view_tuitions, name='view_tuitions'),
    re_path(r'^/unlock_tuition', views.unlock_tuition, name='unlock_tuition'),
    re_path(r'^/change_status', views.change_status, name='change_status'),
    re_path(r'^/view_tuitions$', views.view_tuitions, name='view_tuitions'),


    re_path(r'^/createTuition$', views.createTuition, name='createTuition'),
    re_path(r'^/changeStatus', views.changeStatus, name='changeStatus'),


]
