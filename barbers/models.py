from django.db import models
from cloudinary.models import CloudinaryField

class Barber(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    is_available = models.BooleanField(default=True)  # Add this field