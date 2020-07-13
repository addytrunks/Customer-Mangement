from django import forms
from .models import Order,Customer

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email','phone')

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email','phone')
