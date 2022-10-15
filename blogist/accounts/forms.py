from django import form
from django.contrib.auth.models import User


# login form
class LoginForm(form.Form):
    username = form.CharField()
    password = form.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise form.ValidationError("Invalid Credentials")
        return username

# register form