from django import forms
from phonenumber_field.formfields  import PhoneNumberField
from .fields import ListTextWidget
from .models import Contact, Inquiry

PORTS = (
	'Kandla',
	'Tuna' )

class formContact(forms.ModelForm):
	Name =     forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Email=     forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Phone =    PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'+91 9876543210'}),
                                label='Phone Number(With Country Prifix Code)')
	Message =  forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}))
	class Meta:
	    model = Contact
	    fields = '__all__'

class formInquiry(forms.ModelForm):
	Ship_Name = 			         forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Belonging_Country = 	         forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Type_Of_Water = 		         forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Water_Quantity = 				 forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Service_required_at_which_port =  forms.CharField(required=True,
                              widget=ListTextWidget(
                                                  data_list=PORTS,
                                                  name='ship-list',
                                                  attrs={'class': 'form-control'}))
	Email=					         forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Phone = 				         PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'+91 9876543210'}), label='Contact Number (Please Provide Country Prifix Code)')
	class Meta:
	    model = Inquiry
	    fields = '__all__'
