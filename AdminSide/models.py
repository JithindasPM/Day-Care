from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Vehicles(models.Model):
    Vehicle_Id=models.AutoField(primary_key=True)
    Vehicle_Num=models.CharField(unique=True,null=True,blank=True,max_length=10)
    Model = models.CharField(max_length=50,null=True,blank=True)
    Color = models.CharField(max_length=30, null=True, blank=True)



class Driverdb(models.Model):   
    STATUS_CHOICES = [
        ('NOT_VERIFIED', 'Not Verified'),
        ('VERIFIED', 'Verified'),
        ('REJECTED', 'Rejected'),
    ]
    Name=models.CharField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Mobile=models.CharField(max_length=20,null=True,blank=True)
    Username=models.CharField(max_length=20,null=True,blank=True,unique=True)
    Email=models.EmailField(max_length=20,null=True,blank=True,unique=True)
    Address1=models.CharField(max_length=90,null=True,blank=True)
    Address2=models.CharField(max_length=90,null=True,blank=True)
    Pin_Code=models.CharField(max_length=10,null=True,blank=True)
    License_Number=models.CharField(max_length=20,null=True,blank=True)
    ID_Image=models.ImageField(upload_to="Driver Documents")
    Message=models.CharField(max_length=10,null=True,blank=True)
    Verified=models.CharField(default="Not Verified",null=True,blank=True,choices=STATUS_CHOICES,max_length=100)  
    Vehicle_Num=models.CharField(null=True,blank=True,max_length=10)



class StaffDB(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    Staff_Name=models.CharField(max_length=60,null=True,blank=True)
    Location=models.CharField(max_length=60,null=True,blank=True)
    Phone=models.CharField(max_length=20,null=True,blank=True)
    Address=models.CharField(max_length=90,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Is_Verified=models.CharField(default="Pending",null=True,blank=True,choices=STATUS,max_length=100)
    Leave_Message=models.CharField(max_length=200,null=True,blank=True)


class Plans(models.Model):
    Plan_Name=models.CharField(max_length=20,null=True,blank=True)
    Age_Group=models.CharField(max_length=20,null=True,blank=True)
    Price=models.IntegerField()
    Plan_Description=models.CharField(max_length=200,null=True,blank=True)




