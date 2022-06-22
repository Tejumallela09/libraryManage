from LibMng import views
from django.urls import path,include
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # path('<int:id>/', views.stu_login, name="student_login"),
    # path('<int:id>/', views.emp_login, name="employee_login"),
    path('std_bio<int:id>/', views.std_bio, name="student_login"),
    path('emp_bio<int:id>/', views.emp_bio, name="employee_login"),
    path('library<int:id>/', views.library, name="library"),
    path('std_courses<int:id>/', views.std_courses, name="Courses"),
    path('ins_courses<int:id>/', views.ins_courses, name="course"),


]

