from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('Andaman and Nicobar Island','Andaman and Nicobar Island'),(' Andhra Pradesh ','Andhra Pradesh '),
    ('Arunachal Pradesh ','Arunachal Pradesh'),('Assam ','Assam'),
    ('Bihar ','Bihar'),('Chandigarh ','Chandigarh'),
    ('Chhattisgarh ','Chhattisgarh'),(' Arunachal Pradesh','Arunachal Pradesh'),
    ('Karnataka ','Karnataka'),('Kerala ','Kerala'),
    ('akshadweep ','akshadweep'),('Madhya Pradesh','Madhya Pradesh'),
    ('Manipur','Manipur'),('Maharashtra ','Maharashtra'),
    ('meghalay ','meghalay'),('Mizoram ','Mizoram'),
    ('Nagaland ','Nagaland'),('udisa ','udisa'),
    ('Punjab ','Punjab'),('Rajasthan ','Rajasthan'),
    ('Sikkim','Sikkim'),('Haryana ','Haryana'),
    ('Delhi ','Delhi'),('Goa ','Goa'),
    ('Gujarat','Gujarat'),('Himachal Pradesh ','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir') ,('Jharkhand','Jharkhand'),
    ('Tamilnadu ','Tamilnadu'),('Telangana','Telangana'),
    ('Tripura ','Tripura'),('Uttrakhand ','Uttrakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),('West Bengal','West Bengal')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

def __str__(self):
     return str(self.id)

CATEGORY_CHOICES = (
    ('S','Sunglasses'),
    ('C','Contactlenses'),
    ('E','Eyeeglasses'),
    ('G','Goggles')
)

class Product(models.Model):
     title = models.CharField(max_length=100)
     selling_price=models.FloatField()
     discounted_price=models.FloatField()
     description = models.TextField()
     brand=models.CharField(max_length=100)
     category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
     product_image=models.ImageField(upload_to='productimg')

def __Str__ (self):
      return str (self.id)

class Cart(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity=models.PositiveIntegerField(default=1)

def __str__(self):
   return str(self.id)

@property
def total_cost(self):
  return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
     ('Accepted','Accepted'),
     ('Packed','Packed'),
     ('On the way','On the way'),
     ('Delivered','Delivered'),
     ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    