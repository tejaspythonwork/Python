from django.urls import path
from . import views


urlpatterns = [
    path('add_product/',views.add_product,name ='add_product'),
    path('',views.view_products,name ='view_products'),
    path('delete_product/<int:product_id>/',views.delete_product,name ='delete_product'),
    path('edit_product/<int:product_id>/',views.edit_product,name ='edit_product')
]
