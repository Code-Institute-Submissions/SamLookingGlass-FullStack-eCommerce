from django import forms

# Create your views here.
class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
