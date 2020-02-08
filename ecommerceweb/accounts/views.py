from django.shortcuts import render, redirect, reverse, HttpResponse 
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Forms
from django import forms

class UserLoginForm(forms.Form):
    """Form to login user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser

class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']

# Login Function 
def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) 
        
        # populate the form from what the user has keyed in
        
        if login_form.is_valid():
            # attempt to check the username and password is valid
           
            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('mainapp:home'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {
                  'form':login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })

# Logout Function
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('mainapp:home'))

# Registration function

def register(request):
    form = UserRegistrationForm()
    return render(request, 'register.html', {
        'form':form
    })