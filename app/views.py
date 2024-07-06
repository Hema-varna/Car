from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate   

# Create your views here.


def LoginView(request):
    var=AuthenticationForm()
    context={'form':var}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        usernamet=Register.objects.get(username=username).username
        passwordt=Register.objects.get(username=username).password
        print(usernamet,passwordt)
        if usernamet==username and password==passwordt:
            var=CarTable.objects.all()
            context={
                'var':var
            }
            return render(request,'car.html',context) 
    return render(request,'login.html',context)

def RegisterView(request):
    form=Registerform()
    context={
        'form':form
    }
    if request.method=='POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginView')
    return render(request,'register.html',context)
