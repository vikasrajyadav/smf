from django import forms
from django.contrib.auth.models import User
from smfreal.models import UserProfileInfo
from django import forms
from smfreal.models import Post, Comment,Myuserdb

class myuserdb_form(forms.ModelForm):
    myusername_form = forms.CharField()
    password_form = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = Myuserdb
        fields = ('myusername','user_full_name','user_password','user_email','user_pan_card','user_bank_ifsc','user_bank_account_no','created_date')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
