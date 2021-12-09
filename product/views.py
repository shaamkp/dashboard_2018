import json
from django.shortcuts import render
from django.http.response import JsonResponse

from product.models import Category, Product


def product(request):
    products=Product.objects.all()
    categories=Category.objects.all()

    context = {
        "products":products,
        "categories":categories
    }
    return render(request, "products.html",context=context)


def category(request):
    category_name =request.GET.get('category')
    if category_name:

        if category_name == "All":

            products = Product.objects.all().values()
            data = list(products)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Product.objects.filter(category__name=category_name).exists():
                products = Product.objects.filter(category__name=category_name).values()
                data = list(products)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})
