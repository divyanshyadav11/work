from django import forms
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect,  HttpRequest

from .models import Company
from profiles.models import User


class CompanyForm(forms.Form):
	email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'email'}))
	username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'username'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'firstname'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'lastname'}))	
	title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Company title'}))
	description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Description'}))
	logo = forms.ImageField()

	def save(self, request, commit=True):
		logo = self.cleaned_data['logo']
		email = self.cleaned_data['email']
		title = self.cleaned_data['title']
		username = self.cleaned_data['username']
		last_name = self.cleaned_data['last_name']
		first_name = self.cleaned_data['first_name']
		description = self.cleaned_data['description']
		
		user = User.objects.create(
			password = User.objects.make_random_password(),
			email = email,
			username = username,
			first_name = first_name,
			last_name = last_name,
			role = 'owner'
		)
		
		company = Company.objects.create(
			title = title,
			description = description,
			logo = logo,
			user = user
		)

class UpdateCompanyForm(forms.Form):#TODO: user space after the : in dict
	email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'email'}))
	username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'username'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'firstname'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'lastname'}))	
	title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Company title'}))
	description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Description'}))	
	logo = forms.ImageField(required= False)
	
	def  save(self, request, pk, commit=True):#TODO: Later
		queryset = Company.objects.get(id=pk)
		queryset1 = User.objects.get(email= queryset.user)
		queryset.title = self.cleaned_data['title']
		queryset.description = self.cleaned_data['description']
		queryset.logo = self.cleaned_data['logo']
		if not  self.cleaned_data['logo'] is None:
			queryset.logo = self.cleaned_data['logo']
		queryset1.email = self.cleaned_data['email']
		queryset1.username = self.cleaned_data['username']
		queryset1.first_name = self.cleaned_data['first_name']
		queryset1.last_name = self.cleaned_data['last_name']
		queryset.save()
		queryset1.save()


	








	