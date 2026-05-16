from django.db import models
from django.contrib.auth.models import User

class SimulationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    orders = models.IntegerField()
    workers = models.IntegerField()
    speed = models.IntegerField()
    time_required = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username