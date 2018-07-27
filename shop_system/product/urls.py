from django.conf.urls import url

from product.views import (product_create_view, product_list_view, product_update_view,
				 product_delete_view, category_create_view, category_list_view, 
				 category_update_view,delete_category_view)


urlpatterns = [
    url(r'^$', product_list_view, name='product_list'),
    url(r'^category/$', category_list_view, name='category_list'),
    url(r'^create/$', product_create_view, name='product_create'),
    url(r'^edit/(?P<pk>\d+)$', product_update_view, name='product_update'),    
    url(r'^category_create/$', category_create_view, name='category_create'),
    url(r'^delete/(?P<pk>\d+)$', product_delete_view, name='product_delete'),
    url(r'^delete_category/(?P<pk>\d+)$', delete_category_view, name='delete_category'),
    url(r'^category_update/(?P<pk>\d+)$',  category_update_view, name='category_update'),
]