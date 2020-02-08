"""ecommerceweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 
from accounts.views import login
from cart.views import CartView

# Include all app urls here
urlpatterns = [
    path('admin/', admin.site.urls), #Django Admin Access
    path('', include('products.urls', namespace='mainapp')), #Reference point for mainapp
    path('admin/', admin.site.urls),
    # Path for login
    path('login/', login, name='login'),
    # Path for logout
    # path('logout/', logout, name='logout')

    # Path for carts
    path('cart/', login, name='cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

