from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# any aleration on mddels or to generate table in db..cmd>> python manage.py makemigrations
# and after that >> python manage.py migrate
#  to create an super user/ admin cmd>> python manage.py createsuperuser

STATE_CHOICES = (
  ('Andaman and Nicobar Island','Andaman and Nicobar Island'),
  (' Andhra Pradesh ','Andhra Pradesh '),('Assam ','Assam'),
  ('Arunachal Pradesh ','Arunachal Pradesh'),('Chhattisgarh ','Chhattisgarh'),
  ('Bihar ','Bihar'),('Chandigarh ','Chandigarh'),('Goa ','Goa'),
  (' Arunachal Pradesh','Arunachal Pradesh'),('akshadweep ','akshadweep'),
  ('Karnataka ','Karnataka'),('Kerala ','Kerala'),('Haryana ','Haryana'),
  ('Manipur','Manipur'),('Maharashtra ','Maharashtra'),('meghalay ','meghalay'),
  ('Mizoram ','Mizoram'),('Nagaland ','Nagaland'),('udisa ','udisa'),
  ('Punjab ','Punjab'),('Rajasthan ','Rajasthan'),('Sikkim','Sikkim'),
  ('Delhi ','Delhi'),('Gujarat','Gujarat'),('Himachal Pradesh ','Himachal Pradesh'),
  ('Jammu and Kashmir','Jammu and Kashmir') ,('Jharkhand','Jharkhand'),
  ('Tamilnadu ','Tamilnadu'),('Telangana','Telangana'),('Tripura ','Tripura'),
  ('Uttrakhand ','Uttrakhand'),('Madhya Pradesh','Madhya Pradesh'),
  ('Uttar Pradesh','Uttar Pradesh'),('West Bengal','West Bengal')
)
CITY_CHOICES = (
  ('Ahmednagar','Ahmednagar'),('Akola','Akola'),('Amravati','Amravati'),('Aurangabad','Aurangabad'),
  ('Bhandara','Bhandara'),('Buldhana','Buldhana'),('Dhule','Dhule'),('Hingoli','Hingoli'),
  ('Pune','Pune'), ('Chandrapur','Chandrapur'),('Gondia','Gondia'), ('Gadchiroli','Gadchiroli'),
  ('Jalgaon','Jalgaon'),('Latur','Latur'),('Nanded','Nanded'),('Nandurbar','Nandurbar'),
  ('Jalna','Jalna'),('Mumbai','Mumbai'),('Nashik','Nashik'),('Palghar','Palghar'),
  ('Kolhapur','Kolhapur'), ('Nagpur','Nagpur'),('Osmanabad','Osmanabad'), ('Gadchiroli','Gadchiroli'),
  ('Alirajpur','Alirajpur'),('Anuppur','Anuppur'),('Ashoknagar','Ashoknagar'),('Balaghat','Balaghat'),
  ('Barwani','Barwani'),('Betul','Betul'),('Bhind','Bhind'),('Khandwa','Khandwa'),
  ('Bhopal','Bhopal'), ('Gwalior','Gwalior'),('Narsinghpur','Narsinghpur'), ('Sehore','Sehore'),
  ('Burhanpur','Burhanpur'),('Ujjain','Ujjain'),('Indore','Indore'),('Seoni','Seoni'),
  ('Chhatarpur','Chhatarpur'),('Jabalpur','Jabalpur'),('Sagar','Sagar'),('Satna','Satna'),
  ('Chhindwara','Chhindwara'),('Hoshangabad','Hoshangabad'),('Vidisha','Vidisha'), ('Rewa','Rewa'),        
)

# many to one rel. >> user
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(choices=CITY_CHOICES,max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

# id is converted to string.
    def __str__(self):
      return str(self.id)

# product view
CATEGORY_CHOICES = (
  ('S','Sunglasses'),
  ('C','Contactlenses'),
  ('R','Readinglasses'),
  ('G','Goggles')
)

# if using ImageField we must install PILLOW pakacge to work with images. cmd >> pip install pillow
class Product(models.Model):
  title = models.CharField(max_length=100)
  selling_price=models.FloatField()
  discounted_price=models.FloatField()
  description = models.TextField()
  brand=models.CharField(max_length=100)
  category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
  product_image=models.ImageField(upload_to='productimg')

  def __str__ (self):
    return str(self.id)

# default 1 means that quantity should not be negative no.
class Cart(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  product=models.ForeignKey(Product, on_delete=models.CASCADE)
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

    @property
    def total_cost(self):
      return self.quantity * self.product.discounted_price

    