from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def register_student(request):
    stud = Student()    
    try:
        if request.POST:
            
            print('======Button Clicked====== 1')
            role_1 = request.POST['role']
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            gname = request.POST['gname']
            age = request.POST['age']
            gender = request.POST['gender']
            email = request.POST['email']
            address = request.POST['address']
            mobile = request.POST['mob']
            city = request.POST['city']
            country = request.POST['country']
            state = request.POST['state']
            pin = request.POST['pin']
            # print(role_1)
            profile_image = request.FILES['profileimage']
            print(firstname)
            print(lastname)
            if role_1 == 'Student':
                print('Student Role Selected')
                stud = Student.objects.create(
                                            role = role_1,
                                            fname = firstname,
                                            lname = lastname,
                                            guardian_name = gname,
                                            age = age,
                                            email = email,
                                            address = address,
                                            mob = mobile,
                                            gender = gender,
                                            city = city,
                                            country = country,
                                            state = state,
                                            pin = pin,
                                            pic_student = profile_image,
                                            )
                stud.save()
                context = {
                           'stud' : stud,
                           'smsg' : 'Student Data Has Been Inserted',
                          }        
                # return render(request,'myapp/stud_register.html',context) 
                return render(request,'myapp/login.html',context)
            
            # ==========================================================================
            # ==========================================================================
            else:       
                # stud.save()
                tch = Teacher.objects.create(
                                            
                                            role = role_1,
                                            fname = firstname,
                                            lname = lastname,
                                            guardian_name = gname,
                                            age = age,
                                            email = email,
                                            address = address,
                                            mob = mobile,
                                            gender = gender,
                                            city = city,
                                            country = country,
                                            state = state,
                                            pin = pin,
                                            pic_teacher = profile_image,
                                            )
                context = {
                           'teacher' : tch,
                           'smsg' : 'Teacher Data Has Been Inserted',
                          }        
                return render(request,'myapp/login.html',context) 
            # ==========================================================================
            # ==========================================================================    
            
    except Exception as e:
        print(f'User Already Exists')
        print(f'Exception Occured as = {e}')
    return render(request,'myapp/stud_register.html')



def login(request):
    try:
        if "email" in request.session:
            return HttpResponseRedirect('/index_home/')
        else:
            if request.POST:
                email = request.POST['email']
                role_st_tc = request.POST['role']
                pin = request.POST['pin']

            # std = Student.objects.get(email = email)
            # tid = Teacher.objects.get(email = email)
            # print(role_st_tc.email)
            # print(role_st_tc.pin)

            # if tid.role == 'Teacher':
                 
                if role_st_tc == 'Student':
                     instructors = Teacher.objects.all()
                     stud = Student.objects.get(email = email)
                     print(f'Welcome Student = {stud.email}')
                     request.session['email'] = stud.email
                     context = {
                            'role': 'Student',
                            'sid' : stud,
                            'sname' : stud.fname,
                            'instructors' : instructors,
                            }
                     return render(request,'myapp/index_home.html',context)     
                else:
                    students = Student.objects.all()
                    tid = Teacher.objects.get(email = email)
                    print(f'Welcome Teacher = {tid.email}')
                    request.session['email'] = tid.email
                    context = {
                           'role': 'Teacher', 
                           'tid' : tid,
                           'tname' : tid.fname,
                           'student' : students
                           }
                    return render(request,'myapp/index_home.html',context)    
            return render(request,'myapp/login.html')   
    except:
        return render(request,'myapp/invalid_credential.html')
              
    

def index_home(request):
    if "email" in request.session:
        email = request.session['email']
        try:
            students = Student.objects.all()
            instructors = Teacher.objects.all() 
            stud = Student.objects.get(email = request.session["email"])    
            # enrolled_courses = CoursesEnrolled.objects.filter(st_name__id=2)
            # enrolled_courses = CoursesEnrolled.objects.all()
            enrolled_courses = CoursesEnrolled.objects.filter(st_name=stud)
            # for enrollment in enrolled_courses:
            #     course_name = enrollment.c.course_name  # Accessing course_name via ForeignKey
            #     print(course_name)
            # if enrolled_courses.exists():
            student_email = enrolled_courses.first().st_name.email
            # else:
                # student_email = None
            context = {
                'sid': stud.email if stud.email else None,  # Pass None if student ID is not available
                'role': 'Student',
                'sname' : stud.fname,
                'instructors' : instructors,
                'enrolled_courses' : enrolled_courses,
                'semail' : student_email,
                'students' : students,
                
            }
            return render(request, 'myapp/index_home.html', context)
        except Student.DoesNotExist:
            try:
                students = Student.objects.all()
                teacher = Teacher.objects.get(email = email)
                context = {
                    'tid': teacher.email if teacher.email else None,  
                    'role': 'Teacher',
                    'tname' : teacher.fname,
                    'students' : students
                }
                return render(request, 'myapp/index_home.html', context)
            except Teacher.DoesNotExist:
                return render(request,'myapp/login.html')
        
    else:
        return render(request,'myapp/login.html')
    
def logout(request):
    if "email" in request.session:
        del request.session["email"]
    return HttpResponseRedirect('/')


def myProfile(request):
    if "email" in request.session:
        email = request.session['email']
        try:
            stud = Student.objects.get(email = request.session["email"])    
            context = {
                'sid': stud.email if stud.email else None,  # Pass None if student ID is not available
                'role': 'Student',
                'sname' : stud.fname,
                'stu' : stud
            }
            return render(request, 'myapp/my_profile.html', context)
        except Student.DoesNotExist:
            try:
                teacher = Teacher.objects.get(email = request.session['email'])
                context = {
                    'tid': teacher.email if teacher.email else None,  
                    'role': 'Teacher',
                    'tname' : teacher.fname,
                    'stu' : teacher,
                    't_pic' : teacher.pic_teacher,
                }
                return render(request, 'myapp/my_profile.html', context)
            except Teacher.DoesNotExist:
                print('Teacher not exists')
                return render(request,'myapp/my_profile.html')
        
    else:
        # return render(request,'myapp/login.html') 
        print('email not exists')


def updateProfile(request):        
    if "email" in request.session:
        email = request.session['email']
        try:
            stud = Student.objects.get(email = request.session["email"])
            fname = request.POST['fname']
            
            if "myprofilepic" in request.FILES:
                myprofilepic = request.FILES['myprofilepic']
                stud.pic_student = myprofilepic
                stud.fname = fname
                stud.save()
            stud.fname = fname
            stud.save()    
            context = {
                'sid': stud.email if stud.email else None,  # Pass None if student ID is not available
                'role': 'Student',
                'sname' : stud.fname,
                'stu' : stud
            }
            return render(request, 'myapp/my_profile.html', context)
        except:
            pass

def admin_registration(request):
    if request.POST:
        name = request.POST['aname']
        email = request.POST['aemail']
        password = request.POST['apass']

        admin_data = AdminData.objects.create(name_admin = name,
                                              email = email,
                                              password = password,
                                              )  

        admin_data.save()
        print('======================')
        print('Admin Has been created')
        print('======================')
    return render(request,'myapp/admin_registration.html')
def add_courses(request):
    try:
        if request.POST:
           who = request.POST['who']
           course_name = request.POST['cname']
           course_pic = request.FILES['coursepic'] 
           fees = request.POST['fees']
           duration = request.POST['duration']
           email_already_register = request.POST['regemail']
           lecture_flow = request.FILES.get('lecture_flow') 
           pic = course_pic
           
           add_courses_data = Courses.objects.create(course_assigning_person = who,
                                                     course_name = course_name,
                                                     course_image = pic,
                                                     fees = fees,
                                                     duration = duration,
                                                     course_created_email = email_already_register,
                                                     lecture_flow = lecture_flow,
                                                     )  

        return render(request,'myapp/add_courses.html')
    except Exception as e:       
        print(f'Error = {e}')
        return render(request,'myapp/add_courses.html')
    

def view_courses(request):
    # for popular courses
    try:
        course = Courses.objects.all()
        stud = Student.objects.get(email=request.session['email'])
        context = {
            'course':course,
            'stud' : stud
        }
        print('---------')
        print(course.id)
        for i in course:
            print(i.course_name)
        return render(request,'myapp/courses.html',context)
    except:
        return render(request,'myapp/courses.html',context)
    

def join_course_now(request,course_id,student_id):
    if "email" in request.session:
        crs = Student.objects.get(email = request.session['email'])
        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Courses, id=course_id)
        print(crs.fname)
        print(crs.lname)
        print('*************')
        print(student.fname)
        print(course.course_name)
        print('*************')
        context = {
            'student' : student,
            'course' : course
            }
    
    if request.method == 'POST':
        
        
        try:
            if CoursesEnrolled.objects.filter(c=course, st_name=student).exists():
    
                return render(request, 'myapp/joincourses.html', {
                    'student': student,
                    'course': course,
                    'error': 'You are already enrolled in this course.'
         })
        # print('you are already register')
            else:
                CoursesEnrolled.objects.create(
                c=course,  
                st_name=student,  
                student_name=student.fname, 
                course_name = course.course_name,
                fees_paid=True 
                 )            

            return render(request,'myapp/success.html')   
        except Exception as e:
            print('Exception Occured', 'you already registered')
            return render(request,'myapp/already_register_course.html')
    return render(request,'myapp/join_course_now.html',context)


def course_detail(request,id):
    c_detail = Courses.objects.get(id = id)
    stud_detail = Student.objects.get(email = request.session['email'])
    print(c_detail.course_name)
    print(c_detail.fees)
    context = {
        'course' : c_detail,
        'stud_detail' : stud_detail
    }
    return render(request,'myapp/course_details.html',context)

def success(request):
    return render(request,'myapp/success.html')

def already_register_course(request):
    return render(request,'myapp/already_register_course.html')

def courses_list(request):
    courses = Courses.objects.all()  
    return render(request, 'myapp/courses_list.html', {'courses': courses})

# def edit_course(request,course_id):
#     course = get_object_or_404(Courses, id=course_id)
#     # if request.method == 'POST':
#     #     c_name = request.POST['course_name']
#     #     # if "course_image" in request.FILES:
#     #     #     course_pic = request.FILES['course_image']
#     #     duration = request.POST['duration']
#     #     fees = request.POST['fees']    
#     #     course.save()
#     print(course.course_name)
#     return render(request,'myapp/edit_course.html')


def delete_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_list')
    
 

def edit_course(request, course_id):
    try:
        
        course = Courses.objects.get(id=course_id)
    except Courses.DoesNotExist:
        return HttpResponse('Course not found', status=404)

    if request.method == 'GET':
        
        return render(request, 'myapp/edit_course.html', {
            'course_name': course.course_name,
            'course_image': course.course_image,
            'duration': course.duration,
            'fees': course.fees,
            'course_id': course.id,  
            'lecture_flow' : course.lecture_flow
        })

    elif request.method == 'POST':
        
        course_name = request.POST.get('course_name')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees')
        
        
        course_image = request.FILES.get('course_image', course.course_image)
        flow = request.FILES.get('lecture_flow', course.lecture_flow)
        
        course.course_name = course_name
        course.duration = duration
        course.fees = fees
        course.course_image = course_image
        course.lecture_flow = flow
        course.save()  
        return redirect('courses_list')

    
    return render(request, 'myapp/edit_course.html', {
        'course_name': course.course_name,
        'course_image': course.course_image,
        'duration': course.duration,
        'fees': course.fees
    })    


# def instructor_list(request):
#     instructors = Teacher.objects.all()
#     print('instructor_list.fname')
#     print('called')
#     return render(request,'myapp/index_home.html',{'instructors' : instructors})



def attendence(request):
    stud = CoursesEnrolled.objects.all()
    course = CoursesEnrolled.objects.all()
    context = {'stud' : stud,
               'course' : course
               }
    if request.method == "POST":
        try:
            # Fetch the form data
            sname = request.POST['student_name']  # Student ID
            cname = request.POST['course_name']  # Course ID
            topic_name = request.POST['topicname']
            topic_description = request.POST['topicdescription']
            is_present = 'prsnt' in request.POST  # Checkbox value for attendance

            # Create the attendance record
            StudentAttendence.objects.create(
                stud_name=sname,
                course_name=cname,
                topic_name=topic_name,
                topic_description=topic_description,
                stud_present=is_present
            )

            # Redirect to a submission confirmation page after success
            return render(request, 'myapp/attendence_submitted.html')

        except Exception as e:
            print('******')
            print(e)
            print('******')

    # Render the form if it's a GET request or if there was an error
    return render(request, 'myapp/attendence.html', context)

    
def attendencesubmitted(request):
    return render(request,'myapp/attendence_submitted.html')




def inquery_course(request, course_id, student_id):
    # Get the course and student details
    course = get_object_or_404(Courses, id=course_id)
    student = get_object_or_404(Student, id=student_id)
    inq_date = timezone.now().date()
    
    inq = CourseInquery.objects.create(
            stud_name = student,
            course_name = course,
            inquiry_date = inq_date
    )
        # inq.save()
    context = {
        'course': course,
        'stud': student,
        'inq_date' : inq_date
    }
    return render(request, 'myapp/inquery_course.html', context)


def join_course(request, course_id):
    # Logic for handling joining a course, e.g., redirecting to a registration form
    course = Courses.objects.get(id=course_id)
    return render(request, 'myapp/join_course.html', {'course': course})



def add_lecture_flow(request, course_id):
    course = get_object_or_404(Courses, id=course_id)

    if request.method == 'POST':
        # Check if a file is uploaded
        if 'lecture_flow' in request.FILES:
            course.lecture_flow = request.FILES['lecture_flow']  # Update the lecture_flow field
            course.save()  # Save the course instance with the new PDF

            return redirect('course_detail', course_id=course.id)  # Redirect to course details or another page

    context = {
        'course': course,
    }
    return render(request, 'myapp/add_lecture_flow.html', context)

def read_more(request):
    return render(request,'myapp/read_more.html')

