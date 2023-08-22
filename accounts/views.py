from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
        #عمل هنا تححق علشان لو المستخدم عمل تسجيل دخول بالفعل ميقدرش يشوف صفحة تسجيل الدخول تاني 
    if request.user.is_authenticated:
        return redirect('index')
    else :
        if request.method == 'POST':
            fname = request.POST['fName']
            lName = request.POST['lName']
            age = request.POST['age']
            phone_number = request.POST['phone_number']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            conf_password = request.POST['conf_password']

            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Is Taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This Email is Already taken')
                else :
                    patt= "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                    patt_number = r"\d{11}"
                    patt_age = r"\d{2}"
                    if re.match(patt_age,age):
                        if re.match(patt_number,phone_number):

                            if re.match(patt,email):
                                if re.match(password,conf_password):
                                    user = User.objects.create_user(first_name = fname,last_name = lName,email=email,username=username,password=password)
                                    user.save()
                                    userprofile = UserProfile(user=user,age=age,phone_number=phone_number)
                                    userprofile.save()
                                    messages.success(request,'account Success')
                                    return redirect('login')
                                    
                                else:
                                    messages.error(request,"Password Not Match")

                            else :
                                messages.error(request,"Inavailed Email")
                        else :
                            messages.error(request,"Inavailed Number")
                    else : 
                        messages.error(request,"Wrong Age")






    return render(request,'accounts/Register.html') 

def Login(request):
    #عمل هنا تححق علشان لو المستخدم عمل تسجيل دخول بالفعل ميقدرش يشوف صفحة تسجيل الدخول تاني 
    if request.user.is_authenticated:
        return redirect('index')
    else :
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None :
                if 'rememberme' not in request.POST:
                    request.session.set_expiry(0)
                auth.login(request,user)
                return redirect('index')
            else :
                messages.error(request,"Username Or Password is Invaild")



    return render(request,'accounts/Login.html') 

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')  

@login_required(login_url='login')
def profile(request):
    return render(request,'accounts/profile.html')
        