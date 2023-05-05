from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def home(r):
    return render(r,'home.html',{})
def login1(request):
    x=request.POST.get("username")
    y=request.POST.get("password")
    z=User_Details.objects.filter(username=x,password=y).values()
    print(z)
    if z:
        rr=User_Details.objects.get(username=x)
        request.session['name1']=rr.id
        return render(request,'inhome.html',{'x':id})
    else:
        return render(request,'login.html',{'mess':'Credentials Wrong'})
def signup1(request):
    if request.method=='POST':
        x=UserForm(request.POST or None)
        print(x)
        if x.is_valid:
            x.save()
            return render(request,'login.html')
        else:
            return render(request,'signup.html')
def signup(request):
     return render(request,'signup.html')
def login(y):
    return render(y, 'login.html',{})
def project(request):
    if request.method=="POST":
        x=ProjectForm(request.POST or None)
        if x.is_valid:
            x.save()
            return render(request,"inhome.html")
    else:
        return render(request,"project.html")
    return render(request, 'project.html',{})
def sidebar(sb):
    return render(sb, 'sidebar.html',{})
def todo(request):
    if request.method=='POST':
        x=request.session['name1']
        y=todo1()
        y.idx=x
        y.task=request.POST.get("task")
        y.save()
        return render(request,'inhome.html')
    return render(request, 'todo.html',{})
def inhome(h):
    return render(h, 'inhome.html', {})
def contactus(request):
    if request.method=="POST":
        x=ContactDetails(request.POST or None)
        if x.is_valid:
            x.save()
            return render(request,"inhome.html")
    else:
        return render(request,"contactus.html")
    return render(request, 'contactus.html', {})
def profile(pro):
    y=User_Details.objects.get(id=pro.session['name1'])
    return render(pro, 'profile.html', {'y':y})