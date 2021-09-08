from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    bronze = models.IntegerField(default=0)
    cheers = models.IntegerField(default=0)


class Event(models.Model):
    country1 = models.ForeignKey(Country,related_name="country1",on_delete=models.CASCADE)
    country2 = models.ForeignKey(Country,related_name="country2",on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()
