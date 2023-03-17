from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField('date Published')

class Road(models.Model):
  road_name = models.CharField(max_length=255)
  road_type = models.CharField(max_length=255) 


class Location(models.Model):
  location_name = models.CharField(max_length=255)
  location_longtitude = models.CharField(max_length=255)
  location_latitude = models.CharField(max_length=255)
  location_elevation = models.CharField(max_length=255)

class Vehicle(models.Model):
  vehicle_count = models.CharField(max_length=255)
  vehicle_velocity = models.CharField(max_length=255)

Intensity = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),

)

class Record(models.Model):
  intensity = models.CharField(max_length=255, null=True, choices = Intensity)
  time_date = models.DateTimeField('date Published')
  road= models.ForeignKey(Road, null=True, on_delete=models.CASCADE)
  location= models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
  vehicle= models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
