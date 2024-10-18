from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static



urlpatterns = [
    path('register/',views.register_student,name='reg'),
    path('',views.login,name='login'),
    path('index_home/',views.index_home,name='index_home'),
    path('logout/',views.logout,name = 'logout'),
    path('my_profile/',views.myProfile,name='my_profile'),
    path('update_profile/',views.updateProfile,name='update_profile'),
    path('admin_registration/',views.admin_registration,name='adminreg'),
    path('add_courses/',views.add_courses,name='addcourses'),
    path('view_courses/',views.view_courses,name='viewcourses'),
    path('join_courses/<int:course_id>/<int:student_id>/',views.join_course_now,name = 'joincourses'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('success/',views.success,name = 'success'),
    path('alreadyregisteredcourse/',views.already_register_course,name = 'alreadyregcourse'),
    path('courses_list/', views.courses_list, name='courses_list'),
    path('edit_course/<int:course_id>/',views.edit_course,name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('attendence/',views.attendence,name='attendence'),
    path('attendencesubmitted/',views.attendencesubmitted,name='asubmmited'),
    path('inquery_course/<int:course_id>/<int:student_id>/', views.inquery_course, name='inquery_course'),
    path('add-lecture-flow/<int:course_id>/', views.add_lecture_flow, name='add_lecture_flow'),
    path('course_details/<int:course_id>/',views.course_detail,name='cdetail'),
    path('read_more/',views.read_more,name ='readmore')
] 