from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Product
from .forms import ProductForm


class ProductCreateView(CreateView):
	template_name = "product/edit_product.html"
	model = Product
	form_class =  ProductForm
	success_url = reverse_lazy('product_list')

	def form_valid(self, form):
	   form.instance.user =self.request.user
	   return super().form_valid(form)

product_create_view = ProductCreateView.as_view()

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

product_update_view = ProductUpdateView.as_view()

class ProductDeleteView(DeleteView):
	model = Product    
	success_url = reverse_lazy('product_list')

product_delete_view = ProductDeleteView.as_view()