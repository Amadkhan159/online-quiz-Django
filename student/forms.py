from django import forms
from django.contrib.auth.models import User
from . import models
from quiz import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']

