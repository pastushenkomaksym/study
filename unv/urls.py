from django.urls import path

from . import views

urlpatterns = [
    path('add_class', views.add_clas, name='index'),
    path('add_teacher', views.add_teachers, name='index'),
    path('add_student', views.add_student, name='index'),
]