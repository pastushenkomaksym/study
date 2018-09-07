from django.shortcuts import render
from .forms import TeacherForm, StudentForm, ClasForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages

class ClasView(View):
    form_class = ClasForm
    template_name = 'unv/add_class.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('SUCCESS')
            #messages.SUCCESS(request, 'added success')
        return render(request, self.template_name, {'form': form})


class TeacherView(View):
    form_class = TeacherForm
    template_name = 'unv/add_teacher.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('SUCCESS')
        return render(request, self.template_name, {'form': form})


class StudentView(View):
    form_class = StudentForm
    template_name = 'unv/add_student.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('SUCCESS')
            messages.add_message(request, messages.INFO, 'added success')
        return render(request, self.template_name, {'form': form})
