from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     return render(request,'base.html')
from .models import *

def list(request):
    query = request.GET.get('title')  # รับคำค้นหาจากช่องกรอกคำค้น
    show_emp = Movies.objects.all()

    if query:
        show_emp = Movies.objects.filter(title__icontains=query)

    context = {'Moviesdata': show_emp}
    return render(request, 'list.html', context)

def manage(request):
    show_emp = Movies.objects.all()
    context = {'Moviesdata':show_emp}
    return render(request,'show.html',context)

def addmember(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        # สร้างผู้ใช้ในฐานข้อมูล
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        messages.success(request, 'สมัครสมาชิกสำเร็จ !')
        return redirect('/')
    
    return render(request, 'addmember.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ!')
            return redirect('/')
        else:
            messages.error(request, 'เข้าสู่ระบบผิดพลาด. โปรดตรวจสอบข้อมูลของคุณอีกครั้ง.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return render(request, 'login.html')

