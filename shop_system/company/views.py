from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView

from .models import Company
from profiles.models import User
from product.models import Product
from .forms import CompanyForm, UpdateCompanyForm


class CompanyListView(ListView):
	template_name = "company/companys.html" 
	model = Company
	queryset = Company.objects.all()

company_list_view = CompanyListView.as_view() 

class CompanyCreateView(FormView):
	template_name = "company/edit_company.html"
	form_class = CompanyForm
	success_url = reverse_lazy('company_list')
  
	def form_valid(self, form):
		form.save(self.request)
		return super().form_valid(form) 
  
company_create_view = CompanyCreateView.as_view()

class CompanyUpdateView(FormView):
	template_name = "company/ajax.html"
	form_class = UpdateCompanyForm	
	success_url = reverse_lazy('company_list')
	
	def get_initial(self):		
		initial = super(CompanyUpdateView, self).get_initial()
		queryset = Company.objects.get(id = self.kwargs['pk'])
		queryset1 = User.objects.get(email = queryset.user)
		initial['logo'] = queryset.logo
		initial['title'] = queryset.title
		initial['email'] = queryset1.email
		initial['username'] = queryset1.username
		initial['last_name'] = queryset1.last_name
		initial['first_name'] = queryset1.first_name
		initial['description'] = queryset.description
		return initial
				  
	def post(self,request, pk):
		form_class = self.get_form_class()
		form = self.get_form(form_class)   
		if form.is_valid(): 
			form.save(self.request,pk)      
			return super().form_valid(form)    
  
company_update_view = CompanyUpdateView.as_view()

class CompanyDeleteView(DeleteView):
	model = Company   
	success_url = reverse_lazy('company_list')

company_delete_view = CompanyDeleteView.as_view()

class ShowProduct(View):
	
	def get(self,request,name):
		queryset = Product.objects.filter(user__in=name)
		print(queryset)
		return render(request,'company/cproducts.html' ,{'object_list':queryset})
show_products = ShowProduct.as_view()