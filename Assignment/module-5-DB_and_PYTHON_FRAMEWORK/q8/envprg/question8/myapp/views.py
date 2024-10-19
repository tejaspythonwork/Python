from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *

# Create your views here.

def add_product(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_image = request.FILES['productimage']
        product_model = request.POST['productmodel']
        product_ram = request.POST['productram']


        print(product_name,product_price,product_model,product_ram,product_id)
        pk = ProductMst.objects.create(product_id=product_id,
                                       product_name = product_name
                                       )

        ProductSubCategory.objects.create(product = pk,
                                          product_price = product_price,
                                          product_image = product_image,
                                          product_model = product_model,
                                          product_ram = product_ram )

        print('Data has been inserted')
        return redirect('view_products') 
    return render(request, 'myapp/add_product.html')


def view_products(request):
    products = ProductSubCategory.objects.all()
    return render(request, 'myapp/view_product.html', {'products': products})
    
def delete_product(request,product_id):
    product = get_object_or_404(ProductSubCategory, id=product_id)
    if request.method == 'POST':
        product.delete()
    return redirect('view_products')    


def edit_product(request,product_id):
    return render(request,'myapp/edit_product.html')