from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control, never_cache
from StudentApp.models import City, Course, Student


# Create your views here.
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def reg_fun(request):
    return render(request, 'register.html',{'data':''})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def regdata_fun(request):
    User_Name = request.POST['username']
    User_Email = request.POST['useremail']
    User_Pswd = request.POST['userpswd']
    if User.objects.filter(Q(username = User_Name) | Q(email=User_Email)).exists():
        return render(request, 'register.html', {'data': 'Username or Email is already existing'})
    else:
        u1 = User.objects.create_superuser(username= User_Name, email= User_Email, password= User_Pswd)
        u1.save()
        return redirect('log')
    # User is a Predefined Table and username, email, password are Column names in the table

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def log_fun(request):
    return render(request, 'login.html', {'data':''})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def logdata_fun(request):
    User_Name = request.POST['username']
    User_Pswd = request.POST['userpswd']
    user1 = authenticate(username=User_Name, password=User_Pswd)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'User is not a Super User'})
    else:
        return render(request, 'login.html', {'data': 'Enter Proper Username and Password'})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def home_fun(request):
    return render(request, 'home.html')

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'add_student.html', {'City_Data':city, 'Course_Data':course, 'data': ''})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def readdata_fun(request):
    s1 = Student()
    s1.Stud_Name = request.POST['sname']
    s1.Stud_Age = request.POST['sage']
    s1.Stud_Phone_No = request.POST['sphnno']
    s1.Stud_City = City.objects.get(City_Name = request.POST['ddlcity'])
    s1.Stud_Course = Course.objects.get(Course_Name = request.POST['ddlcourse'])
    s1.save()
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'add_student.html', {'City_Data':city, 'Course_Data':course, 'data': 'Student Data Inserted Successfully'})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data': s1, 'Data': ''})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    s2 = Student.objects.all()
    return render(request, 'display.html', {'Data': 'Student Data Deleted Successfully', 'data': s2})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def update_fun(request, id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Stud_Name = request.POST['sname']
        s1.Stud_Age = request.POST['sage']
        s1.Stud_Phone_No = request.POST['sphnno']
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        s2 = Student.objects.all()
        return render(request, 'display.html', {'Data': 'Student Data Updated Successfully', 'data': s2})
    return render(request, 'update.html', {'data': s1, 'City_Data':city, 'Course_Data': course})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def forgot_pswd_fun(request):
    if request.method == 'POST':
        User_Name = request.POST['username']
        User_Pswd = request.POST['userpswd']
        if User.objects.filter(username = User_Name).exists():
            u1 = User.objects.get(username= User_Name)
            User_Email = u1.email
            u1.delete()
            u1 = User.objects.create_superuser(username=User_Name, email=User_Email, password=User_Pswd)
            u1.save()
            return render(request, 'login.html', {'data': 'Password Reset Successful'})
        else:
            return render(request, 'resetpswd.html', {'data': 'Enter Proper User Name'})
    return render(request, 'resetpswd.html', {'data': ''})
