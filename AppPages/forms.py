from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from AppAccount.models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email','password','groups']
    