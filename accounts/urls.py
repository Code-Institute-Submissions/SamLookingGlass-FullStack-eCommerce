from django.urls import path, include
from .views import logout, login, profile, register
from products.views import Home

app_name= 'accountsapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Path for login
    path('login/', login, name='login'),
    # Path for logout
    path('logout/', logout, name='logout'),
    # Path for registration
    path('register/', register, name='register'),
    # Path for viewing profile
    path('profile/', profile, name='profile'),
]
