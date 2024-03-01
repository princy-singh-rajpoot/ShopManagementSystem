from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Customer,  Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse  


class ProductView(View):
 def get (self, request): 
  Sunglasses= Product.objects.filter(category='S')
  Contactlenses= Product.objects.filter(category='C')
  Goggles= Product.objects.filter(category='G')
  return render (request,'app/home.html',{'Sunglasses':Sunglasses,'Contactlenses':Contactlenses,'Goggles':Goggles})
  
class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    # print(cart)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    # print(cart_product)
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
        totalamount = amount + shipping_amount 

      data = {
        'quantity' : c.quantity,
        'amount' : amount,
        'totalamount' : totalamount       
      }   
      return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

# mobile page
def Eyeeglasses(request, data=None):
    if data == None:
        Eyeeglasses = Product.objects.filter(category='E')
    elif data == 'Dior' or data == 'Prada':
      Eyeeglasses = Product.objects.filter(category='E').filter(brand=data)
    elif data =='below':
      Eyeeglasses=Product.objects.filter(category='E').filter(discounted_price__lt=5000)
    elif data =='above':
      Eyeeglasses=Product.objects.filter(category='E').filter(discounted_price__gt=5000)
    return render(request,'app/Eyeeglasses.html',{'Eyeeglasses':Eyeeglasses})

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

def checkout(request):
 return render(request, 'app/checkout.html')

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
