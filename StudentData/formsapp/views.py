from django.shortcuts import render,redirect
from django.http import HttpResponse
from formsapp.forms import Userreg,Updatepro
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
	return HttpResponse("welcome formsapp")

def demo(request):
	return render(request,'formsapp/demo.html')

def About(request):
	return render(request,'formsapp/about.html')
def Contact(request):
	return render(request,'formsapp/contact.html')
def Home(request):
	return render(request,'formsapp/home.html')

@login_required
def dashboard(request):
	return render(request,"formsapp/dashboard.html")
@login_required
def Profile(request):
	return render(request,"formsapp/profile.html")	



# def login(request):
# 	return render(request,'formsapp/login.html')

def register(request):
	if request.method=="POST":
		form=Userreg(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponse("Successfully registered")
			messages.success(request,"Successfully registered")
			return redirect('login')
	form=Userreg()
	return render(request,'formsapp/register.html',{'form':form})

@login_required
def updatepro(request):
	if request.method=="POST":
		data=Updatepro(request.POST,instance=request.user)
		if data.is_valid():
			data.save()
			messages.success(request,'Successfully updated')
			return redirect('Profile')
	data=Updatepro(instance=request.user)
	return render(request,'formsapp/updatepro.html',{'data':data})

