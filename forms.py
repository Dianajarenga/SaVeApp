from django import forms
from django.db.models.base import Model
from .models import  RegisteredUser, User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
class UserLogInForm(forms.ModelForm):
    class Meta:
        model=RegisteredUser
        fields="__all__"        