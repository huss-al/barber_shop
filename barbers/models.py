from django.db import models
from cloudinary.models import CloudinaryField

    
class Barber(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    is_available = models.BooleanField(default=True)  # New field for availability

    def __str__(self):
        return self.name
    

class CutType(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name