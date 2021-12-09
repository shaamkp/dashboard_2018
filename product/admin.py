from django.contrib import admin

from product.models import Category, Product


admin.site.register(Product)
admin.site.register(Category)
