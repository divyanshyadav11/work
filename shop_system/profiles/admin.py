from django.contrib import admin

from .models import User, Invoice, ProductInvoice


admin.site.register(User)
admin.site.register(Invoice)
admin.site.register(ProductInvoice)