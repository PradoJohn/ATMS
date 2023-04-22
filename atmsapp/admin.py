from django.contrib import admin

# Register your models here.
from .models import *


<<<<<<< HEAD
admin.site.register(GPSDevice)
admin.site.register(GPSCoordinate)
admin.site.register(Vehicle)
admin.site.register(GPSOperator)
admin.site.register(PollutionSensor)
admin.site.register(PollutionData)
=======


admin.site.register(Road)
admin.site.register(Location)
admin.site.register(GPSDevice)
admin.site.register(GPSVehicle)
admin.site.register(GPSInformation)
admin.site.register(PollutionDetector)
admin.site.register(GPSHolder)
admin.site.register(AirPollutionInformation)
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
