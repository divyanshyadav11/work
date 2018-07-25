from django import forms

from .models import Product, Category

#TODO:Should be this fine in  4 spance
class ProductForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all())

	class Meta:
		model = Product
		fields = ('name','category', 'description', 'price','image') 
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'name of product'}),			
			'description': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Description'}),
			'price': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'price'}),
		        }

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')		
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ('category',) 
		widgets = {
			'category': forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'name of category'}),			
			
		        }