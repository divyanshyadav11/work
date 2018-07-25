from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from profiles.views import landing, search_category, home


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^home/$', landing, name='landing'),
    url(r'^$', home, name='home'),
    url(r'^search/(?P<name>.+)/$', search_category, name='search_category'),
    url(r'^company/', include('company.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^products/', include('product.urls')),
    url(r'^the_shop/', include('profiles.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#TODO: Use urlpatterns list append type with new line