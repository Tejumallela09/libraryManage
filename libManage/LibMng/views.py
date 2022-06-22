from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    return render(request, 'Home.html')

def stu_login(request):
    if request.method == 'POST':
        form1 = Student_login(request.POST)
        if form1.is_valid():
            stu_id = form1.cleaned_data['stu_id']
            password = form1.cleaned_data['password']
            s = authenticate(stu_id=stu_id,password=password)
            if s is not None:
                login(request,s)
                messages.info(request,f"HI !{stu_id}")
                return redirect("Stu_home")
            else:
                messages.info(request,"Invalid !")
            # r = Student(stu_id=stu_id,password=password,)
            # r.save()
            # form1 = Student_login()
    else:
        messages.info(request, "Invalid !")
        form1 =Student_login()
    # std = Student.objects.all()
    # return render(request, 'Stu_login.html', {'form': form1, 'std': std})
    # return render(request, 'stu_bio-data.html', {'std':std})
    return render(request, 'Stu_login.html', {'form': form1})

def emp_login(request):
    if request.method == 'POST':
        form1 = Employee_login(request.POST)
        if form1.is_valid():
            emp_id = form1.cleaned_data['emp_id']
            password = form1.cleaned_data['password']
            r = Instructor(emp_id=emp_id,password=password,)
            r.save()
            form1 = Employee_login()
    else:
        form1 = Employee_login()
    emp = Instructor.objects.all()
    return render(request, 'Emp_login.html', {'form': form1, 'emp': emp})

def stu_home(request,id):
    if request.method == 'POST':
        std= Student.objects.get(pk=id)
    return render(request, 'Stu_home.html', {'std':std})

def std_bio(request,id):
    if request.method == 'POST':
        std= Student.objects.get(pk=id)
    return render(request, 'stu_bio-data.html', {'std':std})

def emp_bio(request,id):
    if request.method=='POST':
        emp=Instructor.objects.get(pk=id)
    return render(request, 'emp_bio-data.html', {'emp': emp})

def library(request,id):
    if request.method=='POST':
        books=Books_borrowed.objects.get(pk=id)
    return render(request, 'books_borrow.html', {'books': books})

def std_courses(request,id):
    if request.method=='POST':
        courses=Student.objects.get(pk=id)
    return render(request, 'stu_courses.html', {'courses': courses})

def ins_courses(request,id):
    if request.method=='POST':
        course = Instructor.objects.get(pk=id)
    return render(request, 'emp_courses.html', {'course': course})