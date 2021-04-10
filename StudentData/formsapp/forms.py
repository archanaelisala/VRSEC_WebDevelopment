from django import forms

from django.forms import ModelForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class Userreg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your confirm password'}))
	
	class Meta:
		
		model=User
		fields= ['username','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'})
		}

class Updatepro(ModelForm):
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first_name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last_name'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter  your Email'})
		}


