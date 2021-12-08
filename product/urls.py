from django.urls import path
from django.conf import settings
from product.views import product

app_name = "product"

urlpatterns = [
    path("",product,name="product")
]