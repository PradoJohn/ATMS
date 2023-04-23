from django.forms import ModelForm
from .models import *

class GPSForm(ModelForm):
    class Meta:
        model = GPSDevice
        fields = '__all__'

class OperatorForm(ModelForm):
    class Meta:
        model = GPSOperator
        fields = '__all__'

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CoordinateForm(ModelForm):
    class Meta:
        model = GPSCoordinate
        fields = '__all__'