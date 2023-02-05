from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
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
    trips = models.IntegerField()
    materials = models.ForeignKey(Material,on_delete=models.CASCADE)
    payment_mode = models.ForeignKey(Payment,on_delete=models.CASCADE)
    datetime = models.DateField(auto_now_add=True,null=True)

