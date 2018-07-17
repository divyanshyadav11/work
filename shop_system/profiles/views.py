from django.views import View
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from product.models import Product
from company.models import Company
from profiles.models import User, Invoice, ProductInvoice


class LandingView(ListView):
    template_name = "profiles/landingpage.html"
    model = Product
    queryset = Product.objects.all().values('name', 'ptype', 'description').distinct()

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
			invoice = Invoice(	
				user=request.user,
				total=amount['total']
							) 
			invoice.save()
			for i in queryset:
				productinvoice = ProductInvoice(
							invoice=invoice,
							product=i.id
										)
				productinvoice.save()
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

class SearchPriceView(View):

	def get(self, request, name ):
		queryset = Product.objects.all().values('name', 'ptype', 'description').distinct()
		queryset1 = Product.objects.filter(name=name)
		users=[]
		for user in queryset1:
			users.append(user.user)	
		queryset2 = Company.objects.filter(user__in=users)
		return render(request,'profiles/landingpage.html' , {'product':queryset, 'price': queryset1,'company':queryset2,'name':name})

SearchPrice = SearchPriceView.as_view()
	