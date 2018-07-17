from django import forms

from .models import Product

#TODO:Should be this fine in  4 spance
class ProductForm(forms.ModelForm):	

	class Meta:
		model = Product
		fields = ('name', 'ptype', 'description', 'price') 
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'name of product'}),
			'ptype': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'type'}),
			'description': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Description'}),
			'price': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'price'}),
		        }