from django.forms import ModelForm
from .models import *

class GPSForm(ModelForm):
    class Meta:
        model = GPSDevice
        fields = '__all__'
