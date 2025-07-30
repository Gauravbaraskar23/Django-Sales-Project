from django.urls import path
from sales_customer.views import customer

urlpatterns = [
    path('' , customer , name = 'customer'),
    
]