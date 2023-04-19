from django.contrib import admin

# Register your models here.
from .models import *




admin.site.register(Road)
admin.site.register(Location)
admin.site.register(GPSDevice)
admin.site.register(GPSVehicle)
admin.site.register(GPSInformation)
admin.site.register(PollutionDetector)
admin.site.register(GPSHolder)
admin.site.register(AirPollutionInformation)