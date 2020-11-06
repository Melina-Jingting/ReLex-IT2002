from django import forms
from django.contrib.auth.forms import UserCreationForm
from AppSeeker.models import Seeker, SeekerSkill
from AppCompany.models import Company



class SeekerFilterForm(forms.ModelForm):
    name = forms.CharField()
    industry = forms.CharField()
    class Meta:
        model = Seeker
        fields = ['name','industry']
    

class SeekerFilterForm(forms.ModelForm):
    skill = forms.CharField(required=False)
    class Meta:
        model = SeekerSkill
        fields = ['skill']


class CompanyFilterForm(forms.ModelForm):
    industries = ["Hospital","Financial","Real","Market","Pharmaceuticals",
    "Cosmetics","Public","Accounting","Media","Medical","Staffing","Retail","Internet",
    "Management","Insurance","Computer","Chemicals","Investment","not","Marketing",
    "Telecommunications","Banking","Law","Automotive","Industrial","International",
    "Higher","Biotechnology","Food","Semiconductors","Human","Information",]
    sizes = ["11-50","11-50 ","501-1,000 ","51-200 ","10001+ ","5,001-10,000 ",
    "2-10 ","1,001-5,000 ","201-500 "]
    locations = ["Greater Osaka Area","Central Singapore Community Development Council, Singapore",
    "Singapore, SG","Singapore, Singapore","Singapore, Singapore Remote"]
    industry = forms.ChoiceField(choices = industries)
    size = forms.ChoiceField(choices = sizes)
    location = forms.ChoiceField(choices = locations)
    
    class Meta:
        model = Company
        fields = ['industry','size','location']

        