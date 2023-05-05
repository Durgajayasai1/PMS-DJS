from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = ['id','username','email','password']
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project_Details
        fields=['id','project','type','start','end','priority','description']
class ContactDetails(forms.ModelForm):
    class Meta:
        model=contact_us
        fields=['id','name','email','description']