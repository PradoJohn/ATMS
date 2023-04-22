from django.db import models

# GPS SENSOR MODELS 

class GPSDevice(models.Model):
  STATUS = [
<<<<<<< HEAD
    ('Standby', 'Standby'),
    ('Malfunctioned', 'Malfunctioned'),
    ('Deployed', 'Deployed'),
  ]
  name = models.CharField(max_length=255, null=True)
  imei = models.CharField(max_length=255, null=True)
  model = models.CharField(max_length=255, null=True)
=======
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
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
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

class GPSCoordinate(models.Model):
  gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)
  speed = models.CharField(max_length=255)
  date = models.DateField(auto_now_add=True, null=True)
  time = models.TimeField(auto_now_add=True, null=True)

  def __str__(self):
<<<<<<< HEAD
    return self.gpsdevice.name

class Vehicle(models.Model):
  plate_no = models.CharField(max_length=255, null=True)
  description = models.CharField(max_length=255, null=True)

  def __str__(self):
      return self.plate_no


class GPSOperator(models.Model):
  gps = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  plate_number = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
  operator = models.CharField(max_length=255, null=True)
  contact = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.gps.name
  

# Pollution Sensors Models

class PollutionSensor(models.Model):
  STATUS = [
    ('Standby', 'Standby'),
    ('Malfunctioned', 'Malfunctioned'),
    ('Deployed', 'Deployed'),
  ]
  name = models.CharField(max_length=255, null=True)
  product_model = models.CharField(max_length=255, null=True)
  description = models.CharField(max_length=255, null=True)
  status = models.CharField(max_length=255, null=True, choices=STATUS, default='Standby')
=======
      return self.gpsdevice.name

class GPSVehicle(models.Model):
  plate = models.CharField(max_length=255, null=True)
  make = models.CharField(max_length=255, null=True)
  model = models.CharField(max_length=255, null=True)
  year = models.CharField(max_length=255, null=True)
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea

  def __str__(self):
      return self.plate

<<<<<<< HEAD
class PollutionData(models.Model):
  p_sensor = models.ForeignKey(PollutionSensor, null=True, on_delete=models.CASCADE)
=======

class GPSHolder(models.Model):
  gpsdevice = models.ForeignKey(GPSDevice, null=True, on_delete=models.CASCADE)
  plate = models.ForeignKey(GPSVehicle, null=True, on_delete=models.CASCADE)
  operator = models.CharField(max_length=255, null=True)
  contact = models.CharField(max_length=255, null=True)
  def __str__(self):
    return self.gpsdevice.name
  
class AirPollutionInformation(models.Model):
  pollution_detector = models.ForeignKey(PollutionDetector, null=True, on_delete=models.CASCADE)
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
  pm = models.FloatField(null=True)
  gaseous = models.CharField(max_length=255, null=True)
  meteorological = models.CharField(max_length=255, null=True)
  other_pollutants = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
<<<<<<< HEAD
    return self.p_sensor.name

=======
    return self.pollution_detector.name

class Road(models.Model):
  road_name = models.CharField(max_length=255, null=True)
  road_type = models.CharField(max_length=255, null=True) 

class Location(models.Model):
  name = models.CharField(max_length=255, null=True)
  longitude = models.CharField(max_length=255, null=True)
  latitude = models.CharField(max_length=255, null=True)
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
    
