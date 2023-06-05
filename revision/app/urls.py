from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
   
    path('', views.insert, name='insert'),
    path('show/', views.show, name='show' ),
    path('delete/<int:student_id>/', views.delete, name="delete"),
    path('edit/<int:student_id>/', views.edit, name="edit"),
    path('update/<int:student_id>', views.updated, name='update')
]