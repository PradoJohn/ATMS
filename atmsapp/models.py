from django.db import models



class GPSDevice(models.Model):
  STATUS = [
    ('Standby','Standby'),
    ('Reparing','Reparing'),
    ('Malfunctioned','Malfunctioned'),
    ('Deployed','Deployed'),
  ]
  name = models.CharField(max_length=255, null=True)
  IMEI_number = models.CharField(max_length=255, null=True)
  product_model = models.CharField(max_length=255, null=True)
  network = models.CharField(max_length=255, null=True)
  SIM_number = models.CharField(max_length=255, null=True)
  main_function = models.CharField(max_length=255, null=True)
  status = models.CharField(max_length=255, null=True, choices=STATUS, default='Standby')

  def __str__(self):
    return self.name
  
class PollutionDetector(models.Model):
  STATUS = [
    ('Standby','Standby'),
    ('Reparing','Reparing'),
    ('Malfunctioned','Malfunctioned'),
    ('Deployed','Deployed'),
  ]
  name = models.CharField(max_length=255, null=True)
  product_model = models.CharField(max_length=255, null=True)
  description = models.CharField(max_length=255, null=True)
  status = models.CharField(max_length=255, null=True, choices=STATUS, default='Standby')
  def __str__(self):
    return self.name

class GPSInformation(models.Model):
  gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)
  speed = models.CharField(max_length=255)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
      return self.gpsdevice.name

class GPSVehicle(models.Model):
  plate = models.CharField(max_length=255, null=True)
  make = models.CharField(max_length=255, null=True)
  model = models.CharField(max_length=255, null=True)
  year = models.CharField(max_length=255, null=True)

  def __str__(self):
      return self.plate


class GPSHolder(models.Model):
  gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  plate = models.ForeignKey(GPSVehicle, null=True, on_delete=models.CASCADE)
  operator = models.CharField(max_length=255, null=True)
  contact = models.CharField(max_length=255, null=True)
  def __str__(self):
    return self.gpsdevice.name
  
class AirPollutionInformation(models.Model):
  pollution_detector = models.ForeignKey(PollutionDetector, null=True, on_delete=models.CASCADE)
  pm = models.FloatField(null=True)
  gaseous = models.CharField(max_length=255, null=True)
  meteorological = models.CharField(max_length=255, null=True)
  other_pollutants = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.pollution_detector.name

class Road(models.Model):
  road_name = models.CharField(max_length=255, null=True)
  road_type = models.CharField(max_length=255, null=True) 

class Location(models.Model):
  name = models.CharField(max_length=255, null=True)
  longitude = models.CharField(max_length=255, null=True)
  latitude = models.CharField(max_length=255, null=True)
    
