from django.conf.urls import url

from profiles.views import SearchPrice, buyproduct, invoiceview, ShowProductInvoice


urlpatterns = [    
    url(r'^price/(?P<name>.+)/$', SearchPrice, name='show_price'),
    url(r'^buy/(?P<name>.+)/$', buyproduct, name='Buy_product'),    
    url(r'^invoice/$', invoiceview, name='show_invoice'),
    url(r'^productinvoice/(?P<ids>.+)/$', ShowProductInvoice, name='show_product_invoice'),
]