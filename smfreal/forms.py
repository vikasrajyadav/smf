from django import forms
from django.contrib.auth.models import User
from smfreal.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = User
        fields = ('username','email','password','firstname','lastname')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
