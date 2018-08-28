from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator


class Persona(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^380\d{9}$', message='Phone number must be entered in format 380XXXXXXXXX')
    phone_number = models.CharField(validators=[phone_regex], max_length=13)

    class Meta:
        abstract = True



class Teacher(Persona):
    subj = models.CharField(max_length=20)

    def __str__(self):
        return f"({self.first_name},{self.last_name},{self.email},{self.subj},{self.phone_number})"


class Clas(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.name})"


class Student(Persona):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.first_name},{self.last_name},{self.email},{self.avg_mark},{self.phone_number})"
