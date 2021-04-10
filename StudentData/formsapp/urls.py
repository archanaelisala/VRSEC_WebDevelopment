from django.urls import path
from formsapp import views
from django.contrib.auth import views as v

urlpatterns = [
path('hello/',views.hello,name='hello'),
path('demo/',views.demo,name='demo'),
path('about/',views.About,name='About'),
path('contact/',views.Contact,name='Contact'),
path('home/',views.Home,name='Home'),
path('path/',views.Profile,name='Profile'),
#path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
path('dashboard/',views.dashboard,name='dashboard'),
path('updatepro/',views.updatepro,name='updatepro'),
path('login/',v.LoginView.as_view(template_name='formsapp/login.html'),name='login'),
path('logout/',v.LogoutView.as_view(template_name='formsapp/logout.html'),name='logout'),




]