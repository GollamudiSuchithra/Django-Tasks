from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
	if request.method=="POST":
		#print(request.POST)
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST.get('email')
		phno = request.POST['phno']
		gender = request.POST['gender']
		address = request.POST['address']
		Languages = request.POST.getlist('Languages')
		#print(uname,rollno,email)
		data = {'firstname':fname,'lastname':lname,'email':email,'phoneno':phno,'gender':gender,'address':address,'Languages':Languages}
		return render(request,'html/show.html',data)
	return render(request,'html/register.html')

def registerboot(request):
	if request.method=="POST":
		#print(request.POST)
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST.get('email')
		phno = request.POST['phno']
		gender = request.POST['gender']
		address = request.POST['address']
		Languages = request.POST.getlist('Languages')
		#print(uname,rollno,email)
		data = {'firstname':fname,'lastname':lname,'email':email,'phoneno':phno,'gender':gender,'address':address,'Languages':Languages}
		return render(request,'html/show.html',data)

	return render(request,'html/registerboot.html')

def login(request):
	return render(request,'html/login.html')
	return render(request,'html/profile.html')

def loginboot(request):
	return render(request,'html/loginboot.html')

	return render(request,'html/profile.html')
	