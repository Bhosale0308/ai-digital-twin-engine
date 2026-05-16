from django.db import models

class Simulation(models.Model):
    name = models.CharField(max_length=100)
    orders = models.IntegerField()
    workers = models.IntegerField()
    speed_per_worker = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name