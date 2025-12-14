from django.db import models


# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    url_image =models.URLField(max_length=200, blank=True)

    # É o id_category
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE, 
        related_name='products',
        null=True, blank=True
        )
    
    # É o id_supplier
    supplier = models.ForeignKey(
        'Supplier', 
        on_delete=models.CASCADE, 
        related_name='products',
        null=True, blank=True
        )

    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name  

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name      