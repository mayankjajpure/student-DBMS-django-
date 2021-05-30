from django.shortcuts import render,redirect
from stu_records.models import students
from django.contrib import messages
from stu_records.forms import strecord
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



def loginuser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('passward')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'front.html')

        else:return render(request,'login.html')

    
    return render(request,'login.html')

def front(request):
    if request.user.is_authenticated:
        return render(request,'front.html')
    else:return redirect('/login')
        
    

def home(request):
    obj=students.objects.all()
    search_input=request.GET.get('search-area')
    if search_input:
        obj=students.objects.filter(stname__icontains=search_input)
    return render(request,'home.html',{'records':obj})

def addnew(request):
    if request.method=="POST":
        obj=students()
        obj.stname=request.POST.get('stname')
        obj.stemail=request.POST.get('stemail')
        obj.stphone=request.POST.get('stphone')
        obj.save()
        messages.info(request,"data "+obj.stname+"added succesfully")

    return render(request,'add.html')

def delete(request,id):
    obje=students.objects.get(id=id)
    obje.delete()

    newdata=students.objects.all()
    return render(request,'home.html',{'records':newdata})

def update(request,id):
    update=students.objects.get(id=id)
    form=strecord(request.POST,instance=update)
    data={
        'records':update,
        'bool':False
    }
    if form.is_valid():
        form.save()
        messages.SUCCESS(request,"data  updated succesfully")
    return render(request,"update.html",data)