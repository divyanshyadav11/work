from django.conf.urls import url

from product.views import (product_create_view, product_list_view, product_update_view,
				 product_delete_view)


urlpatterns = [
    url(r'^$', product_list_view, name='product_list'),
    url(r'^create/$',  product_create_view, name='product_create'),
    url(r'^edit/(?P<pk>\d+)$', product_update_view, name='product_update'),
    url(r'^delete/(?P<pk>\d+)$', product_delete_view, name='product_delete'),
]