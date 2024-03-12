from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Customer,  Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
 def get(self, request): 
  Sunglasses= Product.objects.filter(category='S')
  Contactlenses= Product.objects.filter(category='C')
  Goggles= Product.objects.filter(category='G')
  Readinglasses= Product.objects.filter(category='R')
  return render (request,'app/home.html',{'Sunglasses':Sunglasses,'Contactlenses':Contactlenses,'Readinglasses':Readinglasses,'Goggles':Goggles})
 
 def post(self, request): 
    search_query = request.POST['search_query']
        # Filter your model by the search query
    Sunglasses= Product.objects.filter(category='S',title__icontains=search_query)    
    Contactlenses= Product.objects.filter(category='C',title__icontains=search_query)
    Goggles= Product.objects.filter(category='G',title__icontains=search_query) 
    Readinglasses= Product.objects.filter(category='R',title__icontains=search_query) 
    return render (request,'app/home.html',{'Sunglasses':Sunglasses,'Contactlenses':Contactlenses,'Readinglasses':Readinglasses,'Goggles':Goggles})
 
class ProductDetailView(View):
  def get(self,request,pk):
    product = Product.objects.get(pk=pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
      item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

@login_required
def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    # print(cart)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
      for p in cart_product :
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
        totalamount = amount + shipping_amount 
      return render(request, 'app/addtocart.html', {'carts':cart,'totalamount':totalamount,'amount':amount})
    else :
      return render(request, 'app/emptycart.html',)
    
def plus_cart (request):
  if request.method=='GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product :
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount

    data = {
      'quantity' : c.quantity,
      'amount' : amount,
      'totalamount' :  amount + shipping_amount        
    }   
    return JsonResponse(data)
    
def minus_cart (request):
  if request.method=='GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product :
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      
    data = {
      'quantity' : c.quantity,
      'amount' : amount,
      'totalamount' : amount + shipping_amount   
    }   
    return JsonResponse(data)
    
@login_required
def remove_cart (request):
  if request.method=='GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product :
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount

    data = {
      'amount' : amount,
      'totalamount' : amount + shipping_amount      
    }   
    return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
  op = OrderPlaced.objects.filter(user=request.user)
  return render(request, 'app/orders.html',{'order_placed':op})

@login_required
def payment_done(request):
  user = request.user
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=user)
  for c in cart:
    OrderPlaced(user=user, customer=customer, product=c.product,quantity=c.quantity).save()
    c.delete()
    return redirect("orders")
  
@login_required 
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user)
 cart_items = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.0
 totalamount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product :
  for p in cart_product:
    tempamount =(p.quantity * p.product.discounted_price)
    amount += tempamount
  totalamount = amount + shipping_amount
 return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})
  
# mobile page
def Readingglasses(request, data=None):
    if data == None:
      Readingglasses = Product.objects.filter(category='R')
    elif data == 'Dior' or data == 'Prada':
      Readingglasses = Product.objects.filter(category='R').filter(brand=data)
    elif data =='below':
      Readingglasses=Product.objects.filter(category='R').filter(discounted_price__lt=5000)
    elif data =='above':
      Readingglasses=Product.objects.filter(category='R').filter(discounted_price__gt=5000)
    return render(request,'app/Readingglasses.html',{'Readingglasses':Readingglasses})

# Goggles
def Goggles(request, data=None):
    if data == None:
      Goggles = Product.objects.filter(category='G')
    elif data == 'Dior' or data == 'Prada':
      Goggles = Product.objects.filter(category='G').filter(brand=data)
    elif data =='below':
      Goggles=Product.objects.filter(category='G').filter(discounted_price__lt=5000)
    elif data =='above':
      Goggles=Product.objects.filter(category='G').filter(discounted_price__gt=5000)
    return render(request,'app/Goggles.html',{'Goggles':Goggles})

def Sunglasses(request, data=None):
  if data == None:
    Sunglasses = Product.objects.filter(category='S')
  elif data == 'Dior' or data == 'Prada':
    Sunglasses = Product.objects.filter(category='S').filter(brand=data)
  elif data =='below':
    Sunglasses=Product.objects.filter(category='S').filter(discounted_price__lt=5000)
  elif data =='above':
    Sunglasses=Product.objects.filter(category='S').filter(discounted_price__gt=5000)
  return render(request,'app/Sunglasses.html',{'Sunglasses':Sunglasses})

def Contactlenses(request, data=None):
    if data == None:
      Contactlenses = Product.objects.filter(category='C')
    elif data == 'Dior' or data == 'Prada':
      Contactlenses = Product.objects.filter(category='C').filter(brand=data)
    elif data =='below':
      Contactlenses=Product.objects.filter(category='C').filter(discounted_price__lt=5000)
    elif data =='above':
      Contactlenses=Product.objects.filter(category='C').filter(discounted_price__gt=5000)
    return render(request,'app/Contactlenses.html',{'Contactlenses':Contactlenses})

class CustomerRegistrationView(View):
  def get(self, request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html',{'form':form})
  
  def post(self, request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      # messges 
      # messages.success(request,'Congratulations!! Registered Succesfully') till2:36
      form.save()
    return render(request,'app/customerregistration.html',{'form':form}) 

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get (self, request):
   form = CustomerProfileForm()
   return render (request, 'app/profile.html',{'form':form,'active':'btn-primary'})   

 def post (self,request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
    usr = request.user
    name = form.cleaned_data['name']
    locality = form.cleaned_data['locality']
    city = form.cleaned_data['city']
    state = form.cleaned_data['state']
    zipcode = form.cleaned_data['zipcode']
    reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
    reg.save()
    messages.success(request,'congratulations')
  return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
 
