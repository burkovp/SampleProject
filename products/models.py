from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null =True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # image = models.ImageField(upload_to='details_images')
