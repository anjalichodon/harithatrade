from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)
class Category(models.Model):
    name=models.CharField(max_length=40)

class Sub_category(models.Model):
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
class Product(models.Model):
    P_name=models.CharField(max_length=200)
    SUB_CATEGORY = models.ForeignKey(Sub_category, on_delete=models.CASCADE,default=1)
    P_image=models.CharField(max_length=200)
    Price=models.BigIntegerField()

class Stock(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    S_quantity=models.BigIntegerField()

class Customer(models.Model):
    C_name=models.CharField(max_length=200)
    C_email=models.CharField(max_length=200)
    C_phn=models.BigIntegerField()
    C_place=models.CharField(max_length=200)
    C_post=models.CharField(max_length=200,default=1)
    c_pin=models.CharField(max_length=200,default=1)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)


class Staff(models.Model):
    E_name=models.CharField(max_length=200)
    E_image=models.CharField(max_length=200)
    E_address=models.CharField(max_length=200)
    E_phn=models.BigIntegerField()
    E_email=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,default=1)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)
class Order(models.Model):
    O_date=models.DateField()
    o_time=models.CharField(max_length=200)
    O_status=models.CharField(max_length=200)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    o_delivery=models.CharField(max_length=255,default=1)
    o_delivery_boy=models.CharField(max_length=255,default=1)

class Cart(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    Cart_quantity=models.BigIntegerField()
    Cart_price=models.BigIntegerField()
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE,default=1)


class Payment(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE,default=1)
    Pay_type=models.CharField(max_length=200)
    Pay_status=models.CharField(max_length=200)
    pay_date=models.CharField(max_length=200,default=1)
    pay_amount=models.CharField(max_length=200,default=1)

class Employee(models.Model):
    E_name=models.CharField(max_length=200)
    E_image=models.CharField(max_length=200)
    E_address=models.CharField(max_length=200)
    E_phn=models.BigIntegerField()
    E_email=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,default=1)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)


class Allocate(models.Model):
    EMPLOYEE=models.ForeignKey(Employee,on_delete=models.CASCADE,default=1)
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE,default=1)

class Rating(models.Model):
    Rating=models.CharField(max_length=200)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    R_date=models.DateField()
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)

class Complaint(models.Model):
    Cmplnt=models.CharField(max_length=200)
    Cmplnt_date = models.CharField(max_length=200,default=1)
    Cmplt_reply=models.CharField(max_length=200)
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    Reply_date=models.CharField(max_length=200,default=1)


