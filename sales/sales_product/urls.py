from django.urls import path
from sales_product.views import product

# app_name = 'sales_product'  #Define namespaces
urlpatterns = [
    path('' , product , name = 'product'),
    # path('<int:pk>/',views.)
    
]