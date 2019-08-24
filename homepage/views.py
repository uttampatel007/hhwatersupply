from django.shortcuts import render
from .forms import formContact,formInquiry
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def homepage(request):
	return render(request, 'homepage/homepage.html')

def services(request):
	return render(request,'homepage/service.html')

def gallery(request):
	return render(request,'homepage/gallery.html')

def contact(request):
	message = ''
	if request.method == 'POST':
		form = formContact(request.POST)
		if form.is_valid():
			message = 'Thank You For Submitting Contact Form. We Will Reach You Soon. Have A Great Day!'

			Name = form.cleaned_data['Name']
			Email = form.cleaned_data['Email']
			Phone = form.cleaned_data['Phone']
			Message = form.cleaned_data['Message']
			msg = 'Message From Website. \n Name : %s \n Email: %s \n Phone: %s \n Message : %s \n ' %(Name,Email,Phone,Message)
			send_mail(
					'Contact Message From hhwatersupply.com',
					msg,
					settings.EMAIL_HOST_USER,
					['hhwatersupply@gmail.com'],
					fail_silently=True
				)
			form.save()
			form = None

	else:
		form = formContact()

	return render(request, 'homepage/contact.html', {'form':form , 'message':message})

def inquiry(request):
	message = ''
	if request.method == 'POST':
		form = formInquiry(request.POST)
		if form.is_valid():
			message = 'Thank You For Submitting Inquiry Form. We Will Reach You Soon. Have A Great Day!'

			Ship_Name = form.cleaned_data['Ship_Name']
			Belonging_Country = form.cleaned_data['Belonging_Country']
			Type_Of_Water = form.cleaned_data['Type_Of_Water']
			Water_Quantity = form.cleaned_data['Water_Quantity']
			Service_required_at_which_port = form.cleaned_data['Service_required_at_which_port']

			Email = form.cleaned_data['Email']
			Phone = form.cleaned_data['Phone']
			msg = 'Inquiry From Website. \n Ship_Name : %s \n Belonging_Country: %s \n Type_Of_Water: %s \n Water_Quantity: %s \n Service_required_at_which_port: %s \n Email: %s \n Phone: %s \n' %(Ship_Name,Belonging_Country,Type_Of_Water,Water_Quantity,Service_required_at_which_port,Email,Phone)
			send_mail(
					'Inquiry Message From hhwatersupply.com',
					msg,
					settings.EMAIL_HOST_USER,
					['hhwatersupply@gmail.com'],
					fail_silently=True
				)
			form.save()
			form = None

	else:
		form = formInquiry()

	return render(request, 'homepage/inquiry.html', {'form':form , 'message':message})