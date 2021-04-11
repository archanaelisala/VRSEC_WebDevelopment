"""StudentData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from CRUDApp import views

urlpatterns = [
    path('',views.Crudex),
    path('loginpage/',views.Login,name='Login'),
    path('registerpage/',views.Register,name='Register'),
    path('details/',views.Details,name='Details'),
    path('update/<int:id>/',views.Update,name='Update'),
    path('delete/<int:id>/',views.Delete,name='Delete')


]
