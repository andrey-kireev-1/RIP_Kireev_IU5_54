"""RkRIP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from ComputersOS.views import *

urlpatterns = [
    path('', index, name="РК2"),
    path('create_comp/', create_comp),
    path('create_os/', create_os),
    path('edit_comp/<int:id>/', edit_comp),
    path('edit_os/<int:id>/', edit_os),
    path('delete_comp/<int:id>/', delete_comp),
    path('delete_os/<int:id>/', delete_os),
    path('admin/', admin.site.urls),
]
