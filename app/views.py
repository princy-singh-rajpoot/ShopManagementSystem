from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import Customer,  Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm

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
 return render(request,'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

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

def login(request):
 return render(request, 'app/login.html') 

class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request,'app/customerregistration.html',{'form':form})
  
def post(self,request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
    messages.success(request,'Congratulations!! registered succesfully')
    form.save()
  return render(request,'app/customerregistration.html',{'form':form}) 

def checkout(request):
 return render(request, 'app/checkout.html')
    