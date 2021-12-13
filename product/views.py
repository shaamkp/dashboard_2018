import json
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from product.models import Category, Product
from product.forms import ProductForm
from product.functions import generate_form_errors

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
    


def addProduct(request):
    form = ProductForm(request.POST, request.FILES)
    print("=====================================",form.is_valid())
    if form.is_valid():
        form.save()
    return render(request,'add-product.html', {'form' : form})


def delProduct(request,pk):
    product = Product.objects.filter(pk=pk)
    product.delete()

    return redirect("product:product")

def editProduct(request,id):
    product=Product.objects.get(id=id)
    form = ProductForm(instance=product)
    return render(request,"edit-product.html",{ 'product':product,'form':form })

def updateProduct(request,id):
    product=Product.objects.get(id=id)
    form = ProductForm(request.POST, request.FILES, instance=product)

    context={
        "product" : product,
    }

    if form.is_valid():
        form.save()

        return redirect("product:product")
    else:
        print(generate_form_errors(form))

    return render(request,"edit-product.html", context = context)