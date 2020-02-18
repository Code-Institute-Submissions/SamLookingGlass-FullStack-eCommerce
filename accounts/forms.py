from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth import get_user_model

# Create your views here.
class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    first_name = forms.CharField(label='First Name', required= True)
    last_name = forms.CharField(label='Last Name', required= True)
    email = forms.EmailField(max_length=254, label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['first_name','last_name','email', 'username', 'password1', 'password2']

    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data.get('email') #1
        username = self.cleaned_data.get('username')
        #2 check if the email is unique, using the Django ORM
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2        

class UpdateProfile(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user