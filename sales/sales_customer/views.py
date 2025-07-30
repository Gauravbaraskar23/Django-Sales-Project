from django.shortcuts import render,redirect
from sales_customer.models import Customer

def customer(request):
    data = Customer.objects.all()
    if request.method =='POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        customer_instance = Customer(name = name,number = number , email = email , address = address)
        customer_instance.save()
        return redirect('customer')
    return render(request,'customer.html',{'data':data})
# Create your views here.
