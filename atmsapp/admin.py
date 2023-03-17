from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Book)
admin.site.register(Record)
admin.site.register(Road)
admin.site.register(Location)
admin.site.register(Vehicle)
