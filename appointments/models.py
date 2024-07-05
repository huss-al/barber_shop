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
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='appointments_as_client')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='barber_appointments')
    cut = models.ForeignKey(CutType, on_delete=models.CASCADE, related_name='cut_appointments')
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.client.user.username}'s appointment with {self.barber.name}"
