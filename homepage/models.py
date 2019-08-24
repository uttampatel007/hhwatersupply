from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
	Name =     models.CharField(max_length=40,blank=False)
	Email=     models.EmailField(blank=False)
	Phone =    PhoneNumberField()
	Message =  models.TextField(blank=False)
	def __str__(self):
	    return self.Name

class Inquiry(models.Model):
	Ship_Name =                      models.CharField(max_length=40,blank=False)
	Belonging_Country =              models.CharField(max_length=40,blank=False)
	Type_Of_Water =                  models.CharField(max_length=40,blank=False)
	Water_Quantity =                 models.CharField(max_length=40,blank=False)
	Service_required_at_which_port = models.CharField(max_length=40,blank=False)
	Email =                          models.EmailField(blank=False)
	Phone =                          PhoneNumberField()

	def __str__(self):
	    return self.Ship_Name