from django.urls import path, include
from .views import logout, login, profile, register, update
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
    # Path for updating profile
    path('update/', update, name='update'),
]
