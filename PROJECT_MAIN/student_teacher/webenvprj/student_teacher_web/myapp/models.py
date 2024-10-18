from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    gender_choice = [
        ('Select Gender', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    role_choice = [
        ('Select Role', 'Select Role'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        
    ]

    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)
    guardian_name = models.CharField(max_length=35)
    age = models.IntegerField()
    email = models.EmailField(max_length=35,unique=True)
    mob = models.CharField(max_length=10)
    address = models.CharField(max_length=85)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=15)
    pin = models.IntegerField()
    role = models.CharField(choices=role_choice, default='Select Role', max_length=30)
    gender = models.CharField(choices=gender_choice, default='Select Gender', max_length=20)
    pic_student = models.ImageField(upload_to='profiles/' ,default='profiles/pic1.png',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"  # Optional: Helps when printing instances


class Teacher(models.Model):
    # You don't need to redefine the same choices again, you can reuse them from the Student model
    fname = models.CharField(max_length=35,default='abc')
    lname = models.CharField(max_length=35,default='xyz')
    guardian_name = models.CharField(max_length=35,default=25)
    age = models.IntegerField(default=25)
    email = models.EmailField(max_length=35,default='abc@gmail.com',unique=True)
    mob = models.CharField(max_length=12,default='0909090909')
    address = models.CharField(max_length=85,default='Ahm')
    city = models.CharField(max_length=15,default='Ahm')
    state = models.CharField(max_length=25,default='GJ')
    country = models.CharField(max_length=15,default='India')
    pin = models.IntegerField(default=111)
    role = models.CharField(choices=Student.role_choice, default='Select Role', max_length=30)
    gender = models.CharField(choices=Student.gender_choice, default='Select Gender', max_length=20)
    pic_teacher = models.ImageField(upload_to='profiles/' ,default='profiles/pic1.png',null=True,blank=True)
    
    # ForeignKey linking to the Student model
    # teacher_data = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"  # Optional: Helps when printing instances


class AdminData(models.Model):
    name_admin = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=10)

class Courses(models.Model):
    who_assign_course = [
        ('Select who you are', 'Select who you are'),
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),]
    course_assigning_person = models.CharField(choices=who_assign_course,default='Select Who You Are',max_length=55)
    course_name = models.CharField(max_length=65)
    course_image = models.ImageField(upload_to='courseImg/',null=True,blank=True,default='media/courseImg/pic.png')
    duration = models.CharField(max_length=45)
    fees = models.IntegerField()
    course_created_email = models.CharField(max_length=50)
    course_teaching_person = models.CharField(max_length=55,null=True,blank=True,default='Tejas Bhatt')
    lecture_flow = models.FileField(upload_to='pdfs/',blank=True,null=True)

    def __str__(self):
        return f"{self.course_name}"


class CoursesEnrolled(models.Model):
    c = models.ForeignKey(Courses,on_delete=models.CASCADE)
    st_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=65)
    fees_paid = models.BooleanField(default=True)
    course_name = models.CharField(max_length=65,null=True,blank=True)

class StudentAttendence(models.Model):
    course_name = models.CharField(max_length=45,null=True,blank=True)
    stud_name = models.CharField(max_length=55,null=True,blank=True)
    topic_name = models.CharField(max_length=55,null=True,blank=True)
    topic_description = models.CharField(max_length=100,null=True,blank=True)
    stud_present = models.BooleanField(default=True,null=True,blank=True)


class CourseInquery(models.Model):
    stud_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_name = models.ForeignKey(Courses,on_delete=models.CASCADE)
    inquiry_date = models.DateField(default=timezone.now) 

    def __str__(self) -> str:
        return f"{self.stud_name} {self.course_name}"
    
    