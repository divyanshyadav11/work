from django.conf.urls import url

from profiles.views import search_product, buyproduct, invoiceview, ShowProductInvoice


urlpatterns = [    
    url(r'^invoice/$', invoiceview, name='show_invoice'),
    url(r'^buy/(?P<name>.+)/$', buyproduct, name='Buy_product'),    
    url(r'^price/(?P<name>.+)/$', search_product, name='search_product'),
    url(r'^productinvoice/(?P<ids>.+)/$', ShowProductInvoice, name='show_product_invoice'),
]