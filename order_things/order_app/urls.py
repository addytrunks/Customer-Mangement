from django.urls import path
from order_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('customer/<int:pk>',views.customer,name='customer'),
    path('product/',views.product,name='product'),

    path('orderform/',views.orderform,name='order_form'),
    path('updateform/<int:pk>',views.updateform,name='update_form'),
    path('deleteform/<int:pk>',views.deleteform,name='delete_form'),

    path('create-customer/',views.CreateCustomer.as_view(),name='customer_form'),
    path('delete-customer/<int:pk>',views.deletecustomer,name='delete_customer'),
    path('update-customer/<int:pk>',views.UpdateCustomer.as_view(),name='update_customer'),

    path('add_prodcut/',views.CreateProduct.as_view(),name='add_product'),
    path('update_prodcut/<int:pk>',views.UpdateProduct.as_view(),name='update_product'),
    path('delete_prodcut/<int:pk>',views.DeleteProduct.as_view(),name='delete_product'),

]
