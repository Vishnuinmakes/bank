from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth,messages
from . models import Team

# Create your views here.

def index(request):
    object=Team.objects.all()
    return render(request,'index.html',{'res':object})

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/login/application')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
    return render(request, 'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user=User.objects.create_user(username=username,password=password)
        user.save();
        return redirect('/login')

    return render(request,'register.html')

def application(request):
    if request.method == 'POST':
        return redirect("bank_app:form")
    return render(request,'application.html')

def form(request):

    return render(request,'form.html')

def message(request):
    return render(request,'message.html')