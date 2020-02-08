from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

# def logout(request):
#     auth.logout(request)
#     messages.success(request, "You have successfully been logged out")
#     return redirect(reverse('index'))