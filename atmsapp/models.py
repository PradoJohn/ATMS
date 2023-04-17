from django.db import models



class GPSDevice(models.Model):
  name = models.CharField(max_length=255, null=True)
  IMEI_number = models.CharField(max_length=255, null=True)
  product_model = models.CharField(max_length=255, null=True)
  network = models.CharField(max_length=255, null=True)
  SIM_number = models.CharField(max_length=255, null=True)
  main_function = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.name

class GPSInformation(models.Model):
  gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)
  speed = models.CharField(max_length=255)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

class GPSHolder(models.Model):
    gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
    vehicle_operator = models.CharField(max_length=255, null=True)
    vehicle_plate = models.CharField(max_length=255, null=True)
    operator_contact = models.CharField(max_length=255, null=True)


class PollutionDetector(models.Model):
  name = models.CharField(max_length=255, null=True)
  product_model = models.CharField(max_length=255, null=True)
  description = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.name

class AirPollutionInformation(models.Model):
  pollution_detector = models.ForeignKey(PollutionDetector, null=True, on_delete=models.CASCADE)
  pm = models.FloatField(null=True)
  gaseous = models.CharField(max_length=255, null=True)
  gaseous = models.CharField(max_length=255, null=True)
  meteorological = models.CharField(max_length=255, null=True)
  other_pollutants = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)


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

