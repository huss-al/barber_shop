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
    notes = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    cut = models.ForeignKey(CutType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('datetime', 'barber')

    def __str__(self):
        return f"Appointment with {self.client} at {self.datetime}"
