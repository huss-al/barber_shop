from django.db import models
from profiles.models import Profile
from barbers.models import Barber

class CutType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    datetime = models.DateTimeField()
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    barber = models.ForeignKey('barbers.Barber', on_delete=models.CASCADE)
    cut = models.ForeignKey(CutType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment with {self.client} at {self.datetime} for {self.cut}"
