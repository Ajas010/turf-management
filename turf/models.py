from django.db import models  # type: ignore
import turf
from userapp.models import Userprofile

    

class Turfadmin(models.Model):
    STATUS_CHOICE=[
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),

    ]

    Loginid=models.OneToOneField (Userprofile, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    ownername=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    rent=models.CharField(max_length=100,null=True,blank=True)
    openingtime=models.CharField(max_length=100,null=True,blank=True)
    closingtime=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICE,default='pending')
    is_active=models.BooleanField(null=False,blank=True,default=True)


class Product(models.Model):
        Ownerid = models.ForeignKey(Userprofile, on_delete=models.CASCADE, blank=True, null=True)
        turfid = models.ForeignKey(Turfadmin, on_delete=models.CASCADE, blank=True, null=True)
        productname=models.CharField(max_length=250,null=True,blank=True)
        category=models.CharField(max_length=250,null=True,blank=True)
        description=models.CharField(max_length=250,null=True,blank=True)
        image=models.ImageField(upload_to="images/",null=True,blank=True)
        price=models.FloatField(null=True,blank=True)
        quantity=models.CharField(max_length=250,null=True,blank=True)
        status =models.CharField(max_length=50,default=True)
        is_active = models.BooleanField(null=False, blank=True, default=True)
        created_at = models.DateTimeField(auto_now=True)
        updated_at= models.DateTimeField(auto_now=True)


class Slot(models.Model):
        turfid=models.ForeignKey(Turfadmin, on_delete=models.CASCADE, blank=True, null=True)
        timeslot=models.CharField(max_length=1000,null=True,blank=True)
        status =models.CharField(max_length=50,default=False)
        is_active = models.BooleanField(null=False, blank=True, default=True)
        created_at = models.DateTimeField(auto_now=True)
        updated_at= models.DateTimeField(auto_now=True)        
    
  
    


    