from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.surname}"