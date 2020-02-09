from django.urls import path
from . views import Home

app_name= 'mainapp'

urlpatterns = [
    # Path for homepage
    path('', Home.as_view(), name='home'),
]