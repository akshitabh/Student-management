from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.db.models import Q
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
    stu = Addstudents.objects.all()
    addcourse = AddCourse.objects.all()
    return render(request,'viewstudents.html',{'stu': stu,'addcourse':addcourse})
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
def addstudent(request):
    if request.method== 'POST':
        stname=request.POST['name']
        stemail=request.POST['email']
        stmobile=request.POST['mobile']
        stcollege=request.POST['college']
        stdegree=request.POST['degree']
        st_addcourse_id=request.POST['course']
        staddress=request.POST['address']
        stucourse=Addstudents.objects.get(id=st_addcourse_id)
        if Addstudents.objects.filter(semail=stemail).exists():
            messages.error(request,'email is already exist')
            return redirect('/addstudent/')
        elif Addstudents.objects.filter(smobile=stmobile).exists():
            messages.error(request,'mobile number already exists')
            return redirect('/addstudent/')
        else:
            Addstudents.objects.create(sname=stname,
                                       semail=stemail,
                                       smobile=stmobile,
                                       scollege=stcollege,
                                       sdegree=stdegree,
                                       scourse=stucourse,
                                       saddress=staddress,
                                       )
            messages.success(request,'student successfully added')
            stu=Addstudents.objects.all()
            addcourse=Addstudents.objects.all()
            return render(request,'viewstudents.html',{'stu':stu, 'addcourse':addcourse})
    else:
        stu=Addstudents.objects.all()
        addcourse=Addstudents.objects.all()
        return render(request,'viewstudents.html',{'stu':stu, 'addcourse':addcourse})    
def update_course(request,uid):
    update=AddCourse.objects.get(id=uid)
    return render(request,'update_course.html',context={'student':update,})

def updatecourse_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        c_name=request.POST['CourseName']
        c_fees=request.POST['CourseFees']
        c_duration=request.POST['Duration']
        c_desc=request.POST['CourseDesc']
        AddCourse.objects.filter(id=uid).update(course=c_name, fees=c_fees,
                                                 duration=c_duration,
                                                 desc=c_desc)
        return redirect("/courses/")

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains = q) | Q(semail__icontains = q)) |Q(smobile__icontains = q)
        student = Addstudents.objects.filter(multiple_q)
    else:
        student = Addstudents.objects.all()
    context = {'student':student}
    return render(request,'viewstudents.html',context)