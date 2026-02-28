from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=150)
    
    def __str__(self):
        return self.username
    
class Product(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to="product/")
    des = models.TextField()
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.title
    
