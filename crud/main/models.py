from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255,blank=True)  
    firstname = models.CharField(max_length=255,blank=True)  
    lastname = models.CharField(max_length=255,blank=True)
    email= models.EmailField(max_length=254)
    class Meta:  
        db_table = "Users"  

class Logs(models.Model):
    logtype = models.CharField(max_length=100,blank=True)  
    text = models.CharField(max_length=255,blank=True)  
    class Meta:  
        db_table = "logs"  
