from django.urls import path
from webschool import views 
urlpatterns = [
    path('', views.index , name = 'index'),
    path('StudentLogin', views.login_form_student , name = 'login_student'),
    path('TeacherLogin', views.login_form_teacher , name = 'login_teacher'),
    path('TeacherPortal', views.teacher_page , name = 'teacher'),
    path('addlesson', views.lessons , name = 'lesson'),
    path('logout/', views.logout , name = 'logout'),
    path('notes/', views.create_notes , name = 'notes'),
    path('my_notes/', views.my_notes , name = 'my_notes'),
    path('notices/', views.notices , name = 'send_notices'),
    path('pastClass' , views.past_class , name = 'past'),
    path('past_notices/', views.past_notices , name = 'notice')
] 
