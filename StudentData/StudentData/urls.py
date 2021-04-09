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
from django.urls import path,include
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.Sample),
    path('sample2/',views.Sample2),

    #dynamic url mapping
    path('strvalue/<str:name>/',views.Strvalue),
    path('intvalue/<int:n>/',views.Intvalue),
    path('multiple/<str:name1>/<int:num>/',views.Multiple),

    #Templates
    path("basichtml/",views.Basichtml),
    path('basiccss/',views.Basiccss), #css
    path('example/',views.Example),  #css
    path('bootstrapex/',views.Bootstrapex),  #bootstrap


    #login and registrations
    path('login/',views.Login),
    path('register/',views.Register),
    path('formsapp/',include('formsapp.urls')),
]
