from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)   
    name = models.CharField( max_length=50) 
    address = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    updated_by = models.CharField(null=True, max_length=50)
    updated_on = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    def __str__(self):
       return self.student_id