from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username    = forms.CharField()
    password    = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationformm(forms.ModelForm):
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    password1 = forms.CharField(label='Repeat Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password1(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password1']:
            raise forms.ValidationError("Password are not matched")
        return cd['password1']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo']