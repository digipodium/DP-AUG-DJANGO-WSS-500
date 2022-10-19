from django import forms
from django.contrib.auth.models import User


INVALID_USERNAMES = ['admin','administrator','root']

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# register form
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
    
