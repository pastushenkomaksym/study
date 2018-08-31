from django import forms


class Persona(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)
    email = forms.EmailField(label= 'email', max_length=254)
    phone_number = forms.CharField(label='phone_number', max_length=13)


class Teachers(Persona):
    subj = forms.CharField(label='subj', max_length=20)


class Clas(forms.Form):
    name = forms.CharField(label='name', max_length=20)
    teacher = forms.CharField(label='teacher', max_length=20)


class Student(Persona):
    avg_mark = forms.IntegerField(max_value=100)
    clas = forms.CharField(max_length=3)
