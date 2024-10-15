from django.forms import ModelForm
from .models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms


class QuestionForm(ModelForm):
    class Meta:
        model=quiz
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class ContactForm(forms.Form):
    f_name = forms.CharField(max_length=255)
    l_name = forms.CharField(max_length=300)
    email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)