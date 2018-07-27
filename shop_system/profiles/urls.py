from django.conf.urls import url

from profiles.views import search_product, buyproduct, invoiceview, ShowProductInvoice, user_list_view, status, create_cart


urlpatterns = [    
    url(r'^invoice/$', invoiceview, name='show_invoice'),
    url(r'^users/$', user_list_view, name='user_list'),
    url(r'^buy/(?P<name>.+)/$', buyproduct, name='Buy_product'),    
    url(r'^price/(?P<name>.+)/$', search_product, name='search_product'),
    url(r'^create_cart/(?P<name>.+)/$',create_cart, name='search_product'),
    url(r'^productinvoice/(?P<ids>.+)/$', ShowProductInvoice, name='show_product_invoice'),
    url(r'^change_status/(?P<ids>.+)/$', status, name='change_status'),
]