from django.conf.urls import url

from company.views import (company_list_view, company_create_view, company_update_view,
				company_delete_view)


urlpatterns = [
    url(r'^$', company_list_view, name='company_list'),
    url(r'^create/$', company_create_view, name='company_create'),
    url(r'^update/(?P<pk>\d+)$', company_update_view, name='company_update'),
    url(r'^delete/(?P<pk>\d+)$', company_delete_view, name='company_delete'),    
]