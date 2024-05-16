from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)
    trips = models.IntegerField(default=0)
    materials = models.ForeignKey(Material,on_delete=models.CASCADE)
    payment_mode = models.ForeignKey(Payment,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    address = models.TextField(default="")
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.trips} {self.materials} - {self.status}"
    

