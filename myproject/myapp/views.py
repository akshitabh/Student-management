from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
def employees(request):
    return render(request,'employees.html')
def courses(request):
    courses = AddCourse.objects.filter(is_active =True).order_by('id')
    return render(request,'courses.html',{'request':request,'courses':courses})
def signup(request):
    return render(request,'signup.html')
def viewstudents(request):
    return render(request,'viewstudents.html')
def form_data(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=make_password (request.POST['password'])
        if User.objects.filter(email = email).exists():
           messages.error(request,'email already exits')
           return redirect('/signup/') 
        else:
            User.objects.create(name=name,email=email,password=password)
            messages.success(request,'registration successfully')
            return redirect('/')
def login(request):
    if request.method=='POST':
        useremail=request.POST['email']
        user_pwd=request.POST['password']
        if User.objects.filter(email=useremail).exists():
            obj=User.objects.get(email=useremail)
            password=obj.password
            if check_password(user_pwd,password):
                return redirect('/dashboard/')
            else:
                messages.error(request,'password is incorrect')
                return redirect('/')
        else:
            messages.error(request,'email is incorrect')
            return redirect('/')
        
def addcourses(request):
    if request.method =='POST':
       cname= request.POST['coursename']
       cfees= request.POST['coursefees']
       cduration=request.POST['courseduration']
       cdesc=request.POST['coursedesc']
       messages.success(request,'course added succesfully')
       AddCourse.objects.create(course=cname,fees=cfees,duration=cduration,desc=cdesc)
       return redirect('/courses/')

    
def deletecourse(request,pk):
    AddCourse.objects.get(id = pk).delete()
    return redirect('/courses/')