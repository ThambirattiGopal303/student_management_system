
from django.urls import path
from backend.views import home_page,students_details,add_page,add_student,update_page,update_student,delete_student
urlpatterns = [
    path('home',home_page,name="home"),
    path('student',students_details,name='student'),
    path("add_page",add_page,name="add_page"),
    path('add_student',add_student,name="add_student"),
    path('update_page/<int:id>',update_page,name="update_page"),
    path('update_student/<int:id>',update_student,name='update_student'),
    path('delete_student/<int:id>',delete_student,name='delete_student'),
  

   
 
]