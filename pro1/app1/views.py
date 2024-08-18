from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def hview(request):
    return render(request,"app1/home.html",{})
@login_required(login_url="/a2/lv/")
def studview(request):
    form = StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/student_form.html",{"form":form})
@login_required(login_url="/a2/lv/")
def showview(request):
    stud=Student.objects.all()
    print(stud)
    return render(request,"app1/show.html",{"obj":stud})

def updateview(request,pk):
    obj=Student.objects.get(roll=pk)
    form=StudentForm(instance=obj)

    if request.method=="POST":
        form=StudentForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/student_form.html",{"form":form})

def deleteview(request,x):
####confirm page####
    obj=Student.objects.get(roll=x)
    if request.method=="POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})

