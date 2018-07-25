from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Product, Category
from .forms import ProductForm, CategoryForm


class ProductCreateView(CreateView):
	template_name = "product/edit_product.html"
	model = Product
	form_class =  ProductForm
	success_url = reverse_lazy('product_list')	

	def get_form_kwargs(self):
		kwargs = super(ProductCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def form_valid(self, form):
	   form.instance.user =self.request.user
	   return super().form_valid(form)

product_create_view = ProductCreateView.as_view()

class CategoryCreateView(CreateView):
	template_name = "product/category_ajax.html"
	model = Category
	form_class =  CategoryForm
	success_url = reverse_lazy('category_list')	

	def form_valid(self, form):
	   form.instance.user =self.request.user
	   return super().form_valid(form)

category_create_view = CategoryCreateView.as_view()

class CategoryListView(ListView):
	template_name = "product/category.html"
	model = Category
	queryset = Category.objects.all()
	
	def get_queryset(self):
		queryset=super(CategoryListView,self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset

category_list_view = CategoryListView.as_view()

class CategoryUpdateView(UpdateView):
	template_name = "product/category_ajax.html" 
	model = Category
	form_class =  CategoryForm
	success_url = reverse_lazy('category_list')

category_update_view = CategoryUpdateView.as_view()

class ProductListView(ListView):
	template_name = "product/products.html" 
	model = Product
	queryset = Product.objects.all()

	def get_queryset(self):
		queryset=super(ProductListView,self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset

product_list_view = ProductListView.as_view()

class ProductUpdateView(UpdateView):
	template_name = "product/ajax_product.html" 
	model = Product
	form_class =  ProductForm
	success_url = reverse_lazy('product_list')

	def get_form_kwargs(self):
		kwargs = super(ProductUpdateView,self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

product_update_view = ProductUpdateView.as_view()

class ProductDeleteView(DeleteView):
	model = Product    
	success_url = reverse_lazy('product_list')

product_delete_view = ProductDeleteView.as_view()

class DeleteCategoryView(View):
	
	def get(self, request, pk):
		queryset = Product.objects.filter(category=pk)
		if not  queryset :
			queryset1 = Category.objects.all().filter(id=pk)
			print(queryset1)
			queryset1.delete()		
			return HttpResponse('category deleted')
		else:
			s=[]
			s.append("you can't delete this category becuse it consist product like:-</br>")
			for a in queryset:
				s.append(a.name)
				s.append('</br>')
			return HttpResponse(s)

delete_category_view = DeleteCategoryView.as_view()	

