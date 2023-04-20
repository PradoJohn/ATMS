from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(GPSDevice)
admin.site.register(GPSCoordinate)
admin.site.register(Vehicle)
admin.site.register(GPSOperator)
admin.site.register(PollutionSensor)
admin.site.register(PollutionData)