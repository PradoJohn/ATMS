from django.db import models

# GPS SENSOR MODELS 

class GPSDevice(models.Model):
  STATUS = [
    ('Standby', 'Standby'),
    ('Malfunctioned', 'Malfunctioned'),
    ('Deployed', 'Deployed'),
  ]
  name = models.CharField(max_length=255, null=True)
  imei = models.CharField(max_length=255, null=True)
  model = models.CharField(max_length=255, null=True)
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

  def __str__(self):
    return self.name

class PollutionData(models.Model):
  p_sensor = models.ForeignKey(PollutionSensor, null=True, on_delete=models.CASCADE)
  pm = models.FloatField(null=True)
  gaseous = models.CharField(max_length=255, null=True)
  meteorological = models.CharField(max_length=255, null=True)
  other_pollutants = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.p_sensor.name

    
