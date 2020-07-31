from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer,Product,Tag,Order
from .forms import OrderForm,CustomerForm,CustomerUpdateForm
from .filters import OrderFilter
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
def home(request):

    customers = Customer.objects.all()
    orders = Order.objects.all().order_by('-date_created')

    total_orders = orders.count()
    orders_pending = Order.objects.filter(status="Pending").count()
    orders_delivered = Order.objects.filter(status="Delivered").count()

    context = {'customers':customers,'orders':orders,'total_orders':total_orders,
                'orders_pending':orders_pending,'orders_delivered':orders_delivered}

    return render(request,'home.html',context)

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    count = customer.order_set.all().count()

    orderFilter = OrderFilter(request.GET,queryset=orders)
    orders = orderFilter.qs 


    context = {'customer':customer,'orders':orders,'count':count,'form':orderFilter}
    return render(request,'customer.html',context)
    
def product(request):
    products = Product.objects.all()

    context = {'products':products,}
    return render(request,'product.html',context)

def orderform(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    form = OrderForm()
    context = {'form':form}

    return render(request,'order_form.html',context)

def updateform(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method=='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {'form':form}
    return render(request,'order_form.html',context)

def deleteform(request,pk):

    item = Order.objects.get(id=pk)
    if request.method=='POST':
        Order.objects.get(id=pk).delete()
        return HttpResponseRedirect('/')

    return render(request,'delete_form.html',context={'item':item})


class CreateCustomer(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'create_customer.html'
def deletecustomer(request,pk):
    cus = Customer.objects.get(id=pk)

    if request.method == 'POST':
        cus.delete()
        return HttpResponseRedirect('/')

    return render(request,'delete_customer.html',context={'cus':cus})
class UpdateCustomer(UpdateView):
    model = Customer
    form_class = CustomerUpdateForm
    template_name = 'update_customer.html'


class CreateProduct(CreateView):
    model = Product
    fields = ('name','price','description','category','tag')
    template_name = 'add_product.html'
class UpdateProduct(UpdateView): 
    model = Product
    fields = ('price','description','category','tag')
    template_name = 'update_product.html'
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product')
