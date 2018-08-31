from django.shortcuts import render
from .forms import Teachers, Student, Clas


def add_clas(request):
    data = {'text':'Add class', 'form':Clas}
    return render(request, 'unv/add_class.html', data)


def add_student(request):
    data = {'text': 'Add student', 'form': Student}
    return render(request, 'unv/add_student.html', data)


def add_teachers(request):
    data = {'text': 'Add teacher', 'form': Teachers}
    return render(request, 'unv/add_teacher.html', data)



