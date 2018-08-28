from django.contrib import admin

from.models import Student, Teacher, Clas


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    ordering = ('last_name',)
    list_display_links = list_display


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    ordering = ('last_name',)
    list_display_links = list_display


class ClasAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_display_links = list_display


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Clas, ClasAdmin)