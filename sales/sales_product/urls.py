from django.urls import path
from sales_product.views import product


urlpatterns = [
    path('' , product , name = 'product'),
    
]