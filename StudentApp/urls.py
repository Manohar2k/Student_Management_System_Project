from django.urls import path
from StudentApp import views

urlpatterns = [
    path('', views.log_fun, name = 'log'),   # It will redirect to login.html page
    path('reg', views.reg_fun, name = 'reg'),   # It will redirect to register.html page
    path('regdata', views.regdata_fun),  # It will create Super User account
    path('logdata', views.logdata_fun), # It will Login if Superuser account exists
    path('home', views.home_fun, name= 'home'),   # It will redirect to home.html
    path('add_students', views.addstudent_fun, name='add'),   # It will redirect to Add_Student.html
    path('readdata', views.readdata_fun),  # It will record data into Student Table
    path('display', views.display_fun, name= 'display'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('delete/<int:id>', views.delete_fun, name='del'),
    path('logout', views.log_out_fun, name='log_out'),
    path('resetpswd', views.forgot_pswd_fun, name='pswd')
]

