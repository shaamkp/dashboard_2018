from django.urls import path
from django.conf import settings
from product.views import category
from product.views import product
from product.views import addProduct,delProduct, editProduct, updateProduct, Product_view

app_name = "product"


urlpatterns = [
    path("",product,name="product"),
    path("category/",category,name="category"),
    path("addProduct/",addProduct, name="addProduct"),
    path('delProduct/<pk>',delProduct,name="delProduct"), 
    path('editProduct/<int:id>',editProduct,name="editProduct"), 
    path('updateProduct/<int:id>',updateProduct,name="updateProduct"), 
    path('delete/',Product_view.as_view(),name='delete')
]