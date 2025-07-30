from django.shortcuts import render,redirect
from sales_product.models import Product

def product(request):
    data = Product.objects.all()
    if request.method =='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        discount = request.POST.get('discount')
        
        customer_instance = Product(name = name,price = price , quantity = quantity , discount = discount)
        customer_instance.save()
        return redirect('product')
    return render(request,'product.html',{'data':data})
# Create your views here.

