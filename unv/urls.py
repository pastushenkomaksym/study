from django.urls import path
from django.contrib.auth.decorators import login_required
from unv.views import ClasView, TeacherView, StudentView

urlpatterns = [
    path('add_class', ClasView.as_view(), name='class'),
    path('add_teacher', login_required(TeacherView.as_view(), login_url='/login'), name='teacher'),
    path('add_student', StudentView.as_view(), name='student'),
]