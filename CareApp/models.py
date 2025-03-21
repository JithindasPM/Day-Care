from django.db import models
from AdminSide.models import Driverdb
from AdminSide.models import Plans

# Create your models here.
class RegistrationDB(models.Model):
    Id=models.AutoField(primary_key=True)
    Mail=models.EmailField(null=True,blank=True,max_length=30)
    First_Name=models.CharField(null=True,blank=True,max_length=30)
    Last_Name=models.CharField(null=True,blank=True,max_length=30)
    Username=models.CharField(null=True,blank=True,max_length=30,unique=True)
    Parents_Name=models.CharField(null=True,blank=True,max_length=30)
    Phone=models.CharField(null=True,blank=True,max_length=12)
    Address=models.CharField(null=True,blank=True,max_length=100)
    Location=models.CharField(null=True,blank=True,max_length=30)
    Password=models.CharField(null=True,blank=True,max_length=30)
    Pickup_Point=models.CharField(null=True,blank=True,max_length=30)
    Drop_Point=models.CharField(null=True,blank=True,max_length=30)
    Medical_History=models.CharField(null=True,blank=True,max_length=30)
    Alleries=models.CharField(null=True,blank=True,max_length=30)
    Special_Attention=models.CharField(null=True,blank=True,max_length=30)
    Emergency_Procedures=models.CharField(null=True,blank=True,max_length=30)
    Kid_Image=models.ImageField(upload_to="Children Photos",null=True,blank=True)
    driver = models.ForeignKey(Driverdb, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    Temp_Pickup_Point=models.CharField(null=True,blank=True,max_length=300)
    Temp_Drop_Point=models.CharField(null=True,blank=True,max_length=300)
    time_field = models.TimeField(null=True, blank=True)
    date_field=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.Username
    
class Rating(models.Model):
    Username=models.CharField(null=True,blank=True,max_length=30)
    Parents_Name=models.CharField(null=True,blank=True,max_length=30)
    Description=models.CharField(null=True,blank=True,max_length=300)

class Payment(models.Model):
    Customer_ID = models.ForeignKey(RegistrationDB,db_index=True,on_delete=models.CASCADE,to_field='Id')
    Plan_ID = models.ForeignKey(Plans,db_index=True,on_delete=models.CASCADE,to_field='id')
    CardHolder_Name=models.CharField(null=True,blank=True,max_length=900)
    Card_Num=models.CharField(null=True,blank=True,max_length=50)
    Amount=models.CharField(null=True,blank=True,max_length=90)
    Expiry_Date=models.CharField(null=True,blank=True,max_length=50)
    CVV=models.CharField(null=True,blank=True,max_length=10)
    Payment_date = models.DateTimeField(auto_now=True)
