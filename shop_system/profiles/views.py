from django.views import View
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from product.models import Product, Category
from company.models import Company
from profiles.models import User, Invoice, ProductInvoice


class LandingView(View):
	category = Category.objects.order_by('category').values('category').distinct()
	queryset1 = Product.objects.all().order_by('name')
	queryset2 = queryset1.values('name').distinct()
	company = Company.objects.all()
	def get(self, request):		
		return render(request,'profiles/landingpage.html' , {'object_list':self.queryset2,'category':self.category,'images':self.queryset1,'prices':self.company})

landing = LandingView.as_view()

class InvoiceView(ListView):
	template_name = "profiles/invoice.html" 
	model = Invoice
	queryset = Invoice.objects.all()	

invoiceview = InvoiceView.as_view();   

class BuyProductView(View):
	item=[]	
	
	def get(self, request, name):		
		if not request.user.is_authenticated:
			self.item.append(name)
			return redirect('account_login')		
		if name == 'show':
			queryset = Product.objects.filter(id__in=self.item)
			amount = queryset.aggregate(total=Sum('price'))
			return render(request,'profiles/landingpage.html' , {'item':queryset,'sum':amount})
		if name == 'buy':
			queryset = Product.objects.filter(id__in=self.item)
			amount = queryset.aggregate(total=Sum('price'))
			self.item.clear()
			invoice = Invoice.objects.create(	
				user=request.user,
				total=amount['total']
							) 			
			for i in queryset:
				productinvoice = ProductInvoice.objects.create(
							invoice=invoice,
							product=i.id
									)				
			return redirect('landing')
		else:
			self.item.append(name)	
		return redirect('landing')

buyproduct=BuyProductView.as_view()	

class ShowProductInvoiceView(View):

	def get(self, request, ids ):
		queryset1 = Invoice.objects.filter(id=ids)
		queryset = ProductInvoice.objects.filter(invoice__in=queryset1)
		product=[]
		for i in queryset:
			product.append(i.product)
		queryset3 = Product.objects.filter(id__in=product)
		product_list=[]
		for name in queryset3:
			product_list.append(name.name)
			product_list.append('</br>')
		return HttpResponse(product_list)

ShowProductInvoice = ShowProductInvoiceView.as_view()

class SearchProductView(View):
	queryset = Category.objects.all()
	queryset1 = Product.objects.all()
	def get(self, request,name):		
		self.queryset1 = self.queryset1.filter(name=name)
		if  self.queryset1 :
			return render(request,'profiles/landingpage.html' , {'object_list':self.queryset1,'category':self.queryset.order_by('category').values('category').distinct(),'images': Product.objects.all().order_by('name'),'prices': Company.objects.all()})
		else:
			return render(request,'profiles/landingpage.html' , {'error':"Product not found :( ",'category':self.queryset.order_by('category').values('category').distinct()})

search_product = SearchProductView.as_view()

class SearchCategory(View):
	queryset = Category.objects.all()
	queryset1 = Product.objects.all().values('name').distinct()
	def get(self, request,name):
		queryset2 = self.queryset.filter(category=name)
		self.queryset1 = self.queryset1.filter(category__in=queryset2)			
		return render(request,'profiles/landingpage.html' , {'object_list':self.queryset1,'category':self.queryset.order_by('category').values('category').distinct(),'images': Product.objects.all().order_by('name'),'prices': Company.objects.all()})
search_category = SearchCategory.as_view()


def home(request):
	category = Category.objects.order_by('category')
	return render(request,'home.html',{'categorys':category})
	
