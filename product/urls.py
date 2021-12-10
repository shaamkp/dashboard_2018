from django.urls import path
from django.conf import settings
from product.views import category
from product.views import product
from product.views import addProduct

app_name = "product"


urlpatterns = [
    path("",product,name="product"),
    path("category/",category,name="category"),
    path("addProduct/",addProduct, name="addProduct"),
   
]