from django.contrib import admin
from .models import Order,Customer,Product,Tag
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Product)
