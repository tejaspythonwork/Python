from django.contrib import admin
from .models import *


# Register your models here.

# admin.site.register(Student)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AdminData)
admin.site.register(Courses)
admin.site.register(CoursesEnrolled)
admin.site.register(StudentAttendence)
admin.site.register(CourseInquery)