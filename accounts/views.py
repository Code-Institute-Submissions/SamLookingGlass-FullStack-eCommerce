from django.shortcuts import render, redirect, reverse, HttpResponse 
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth import get_user_model
 
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
    User = get_user_model()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        #1 Check if entries on the form are valid
        if form.is_valid(): 
            #1 Create the user
            form.save()
            #2 Check if the user has been created successfully
            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
            if user:
                #3 If the user has been created successfully, attempt to login
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            return redirect(reverse('mainapp:home'))

        #2 If entries are invalid, refresh the form to the view to show the errors
        else:
            return render(request, 'register.html', {
                'form':form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {
            'form':form
        })

@login_required
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {
        'user' : user
    })
