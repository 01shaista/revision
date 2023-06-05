# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Student
from django.utils import timezone
import datetime

# Create your views For Student.
def insert(request):
    context = {'success': False}
    if request.method == "POST":
        # HANDLE THE FORM
          name = request.POST['name']
          if request.POST.get('name')=="":
              return render(request,'insert.html', {'error': True})  
                   
          currentupdate = datetime.date.today() 
          print(name)
          ins = Student(name=name, updated_on=currentupdate)
          ins.save()
          context = {'success': True}  
    return render(request,'insert.html', context)
def show(request):
    allTasks = Student.objects.all()
    context = {'tasks': allTasks}
    return render(request,'show.html', context)
#This Function Will Edit/Update in Student
def delete(request,student_id):
    delete = Student.objects.get(student_id=student_id)
    delete.delete()
    return redirect('/show')
 #This Function Will Edit/Update in Student
def edit(request , student_id):
    print("come here")
    cat = Student.objects.get(student_id=student_id)
    return render(request, 'update.html',{'cat':cat})
def updated(request, student_id):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        name = request.POST['name']
        if request.POST.get('name')=="":
            return render(request, 'update.html',{'error':True})
       
        else:  
            edit = Student.objects.get(student_id = student_id)      
            edit.name = name        
            edit.save()
            return redirect(reverse('show'))
       