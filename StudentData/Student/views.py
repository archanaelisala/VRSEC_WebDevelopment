from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Sample(request):
	return HttpResponse("welcome to Django")
def Sample2(request):
	return HttpResponse("<center><b><h1> welcome to django VRSEC<h1></b></center>")

def Strvalue(request,name):
	return HttpResponse("Welcome to VRSEC..."+name)

def Intvalue(request,n):
	return HttpResponse("Roll num is......%d"%n)

def Multiple(request,name1,num):
	return HttpResponse("Name is....."+name1+"<br>"+"Roll num is....%d"%num)

def Basichtml(request):
	return render(request,'Student/basic.html')

def Basiccss(request):
	return render(request,'Student/basiccss.html')

def Example(request):
	return render(request,'Student/ex.html')

def Bootstrapex(request):
	return render(request,'Student/bootstrap.html')

def Login(request):
	return render(request,'Student/login.html')

def Register(request):
	if request.method == 'POST':
		Fname = request.POST.get('fname')
		print(Fname)
	return render(request,'Student/register.html')