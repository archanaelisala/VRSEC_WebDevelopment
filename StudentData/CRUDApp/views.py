from django.shortcuts import render,redirect
from django.http import HttpResponse
from CRUDApp.models import Studentdata
# Create your views here.
def Crudex(request):
	return HttpResponse("Welcome to CRUD App")


def Login(request):
	return render(request,'crudapp/login.html')


def Register(request):
	if request.method == "POST":
		Fname  = request.POST.get('fname') #getting value from template and storing that value in temporary variable
		Lname = request.POST.get('lname')
		Username = request.POST.get('uname')
		Password = request.POST.get('password')
		Email = request.POST.get('email')
		Mobile = request.POST.get('mobile')
		#print(Fname,Lname,Username)
		#return render(request,'crudapp/showrecord.html',{'Fname':Fname,'Lname':Lname,'Username':Username,'Password':Password,'Email':Email,'Mobile':Mobile})
		Studentdata.objects.create(Firstname=Fname,Lastname=Lname,Username=Username,Password=Password,Email=Email,Mobile=Mobile)
		#return HttpResponse("Record Inserted Successfully")
		return redirect('Details')
	return render(request,'crudapp/register.html')


def Details(request):
	data = Studentdata.objects.all() #reading values from database by using ORM
	return render(request,'crudapp/display.html',{'data':data})



def Update(request,id):
	info = Studentdata.objects.get(id=id)
	if request.method == "POST":
		info.Firstname  = request.POST.get('fname')
		info.Lastname = request.POST.get('lname')
		info.Username = request.POST.get('uname')
		info.Password = request.POST.get('password')
		info.Email = request.POST.get('email')
		info.Mobile = request.POST.get('mobile')
		info.save()
		#return HttpResponse("Updated Successfully")
		return redirect('Details')
	return render(request,'crudapp/update.html',{'info':info})



def Delete(request,id):
	deldata = Studentdata.objects.get(id=id)
	if request.method == 'POST':
		deldata.delete()
		#return HttpResponse("Deleted Successfully")
		return redirect('Details')
	return render(request,'crudapp/delete.html',{'deldata':deldata})

