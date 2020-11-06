from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Seeker, SeekerSkill

class SeekerUpdateForm(forms.ModelForm):
    name = forms.CharField()
    industry = forms.CharField()
    class Meta:
        model = Seeker
        fields = ['name','industry']
    

class SeekerSkillUpdateForm(forms.ModelForm):
    skill = forms.CharField(required=False)
    class Meta:
        model = SeekerSkill
        fields = ['skill']
    

