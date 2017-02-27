from django import forms
from .models import BlogUser

class SignUpForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = BlogUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = BlogUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password']