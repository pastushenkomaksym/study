from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
import logging

logger = logging.getLogger(__name__)


class Persona(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    #phone_regex = RegexValidator(regex=r'^\+380\d{9}$', message='Phone number must be entered in format +380XXXXXXXXX')
    #phone_number = models.CharField(validators=[phone_regex], max_length=13)
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def my_validator(self, val, value_valid):

        is_match = value_valid.search(val)
        return is_match

    first_name_valid = re.compile(r'^[A-z]+\ ?[A-z]?$')
    phone_valid = re.compile(r'\+380\d{9}')
    last_name_valid = re.compile(r'^[A-z]+\-?[A-z]?$')

    def clean(self):
        if not self.my_validator(self.phone_number, self.phone_valid):
            logger.warning('bad user, wrong data number')
            raise ValidationError('not correct number')
        if not self.my_validator(self.first_name, self.first_name_valid):
            logger.warning('bad user, wrong data first name')
            raise ValidationError('not correct first name')
        if not self.my_validator(self.last_name, self.last_name_valid):
            logger.warning('bad user, wrong data last name')
            raise ValidationError('not correct last_name')


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
