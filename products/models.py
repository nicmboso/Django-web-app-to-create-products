from django.db import models

# Create your models here.
class Products(models.Model): # "Products" will be a table in the database 
    Title = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Price = models.CharField(max_length=100)
    Quantity = models.PositiveIntegerField()
    In_stock = models.BooleanField()


    def __str__(self) -> str:
        return self.Title
      
    class Meta:
      verbose_name_plural = "Products"
    