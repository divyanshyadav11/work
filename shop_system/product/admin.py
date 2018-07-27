from django.contrib import admin

from .models import Product, Category, Cart


admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Category)