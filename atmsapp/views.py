from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.forms import inlineformset_factory
from .models import *
from .forms import *
from django.db.models import Prefetch

def index(request):
  return render(request, 'menu/home.html', {})

def home(request):
  return render(request, 'menu/home.html', {})

def dashboard(request):
  return render(request, 'menu/dashboard.html', {})

def traffic_management(request):
  coordinates = GPSCoordinate.objects.order_by('-id')[:5]
  gps_device = GPSDevice.objects.filter(status='Malfunctioned')
  operator = GPSOperator.objects.all()
  context = {
     'coordinates': coordinates,
     'gps_device': gps_device,
     'operator': operator,
  }
  return render(request, 'menu/traffic_management.html', context)

def traffic_management2(request):
  gps_devices = GPSDevice.objects.all()
  gps_last_coordinate = {}
  number = 5
  for gps in gps_devices:
      last_coordinate = gps.gpscoordinate_set.last()
      gps_last_coordinate[gps] = last_coordinate
  context = {
    'number': number,
    'gps_last_coordinate': gps_last_coordinate,
    }
  return render(request, 'menu/traffic_management2.html', context)

def pollution_management(request):
  pollution_data = PollutionData.objects.all()
  pollution_device = PollutionSensor.objects.all()
  context = {
    'pollution_data': pollution_data,
    'pollution_device' : pollution_device,
    }
  return render(request, 'menu/pollution_management.html', context)

def devices(request):
  gps = GPSDevice.objects.all()
  pollution_device = PollutionSensor.objects.all()

  total_gps = gps.count()
  total_pd = pollution_device.count()
  deployed_gps = gps.filter(status='Deployed').count()
  deployed_pd = pollution_device.filter(status='Deployed').count()
  context = {
    'gps': gps,
    'pollution_device': pollution_device,
    'total_gps': total_gps,
    'total_pd': total_pd,
    'deployed_gps': deployed_gps,
    'deployed_pd': deployed_pd,

  }
  return render(request, 'menu/devices.html', context)

def gps_device(request, pk):
  gps = GPSDevice.objects.all()
  gps_device = GPSDevice.objects.get(id=pk)
  gps_coordinate = gps_device.gpscoordinate_set.all()
  context = {
     'gps_device': gps_device,
     'gps_coordinate': gps_coordinate,
     'gps': gps,
  }
  return render(request, 'records/gps_device.html', context)

def pollution_device(request, pk):
  p_device = PollutionSensor.objects.all()
  pollution_device = PollutionSensor.objects.get(id=pk)
  pd_data = pollution_device.pollutiondata_set.all()
  context = {
     'pollution_device': pollution_device,
     'pd_data': pd_data,
     'p_device': p_device,
  }
  return render(request, 'records/pd_device.html', context)

# Add dummy Real-time Data Samples
def add_coordinate(request):
  form = CoordinateForm
  if request.method == 'POST':
    form = CoordinateForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('traffic_management')
  context = {'form': form}
  return render(request, 'records/add_coordinate.html', context)


# ----START of GPS CRUD----

def add_gps(request):
  form = GPSForm
  if request.method == 'POST':
    form = GPSForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('devices')
  context = {
    'form': form,
  }
  return render(request, 'records/add_gps_form.html', context)

def update_gps(request, pk):
  gps_device = GPSDevice.objects.get(id=pk)
  form = GPSForm(instance=gps_device)
  if request.method == 'POST':
    form = GPSForm(request.POST, instance=gps_device)
    if form.is_valid():
      form.save()
      return redirect('devices')
  context ={
    'form': form,
  }
  return render(request, 'records/add_gps_form.html', context)

def delete_gps(request, pk):
  gps_device = GPSDevice.objects.get(id=pk)
  if request.method == 'POST':
    gps_device.delete()
    return redirect('devices')
  context ={
    'gps_device': gps_device,
  }
  return render(request, 'records/delete_gps.html', context)

# ------END OF GPS CRUD -----

# ---Start of Operator CRUD---
def gps_operator(request):
  operator = GPSOperator.objects.all()
  context = {
    'operator': operator,
  }
  return render(request, 'records/gps_operator.html', context)

def add_operator(request):
  form = OperatorForm
  if request.method == 'POST':
    form = OperatorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('gps_operator')
  context = {
    'form': form,
  }
  return render(request, 'records/add_operator_form.html', context)

def update_operator(request, pk):
  operator = GPSOperator.objects.get(id=pk)
  form = OperatorForm(instance=operator)
  if request.method == 'POST':
    form = OperatorForm(request.POST, instance=operator)
    if form.is_valid():
      form.save()
      return redirect('gps_operator')
  context ={
    'form': form,
  }
  return render(request, 'records/add_operator_form.html', context)

def delete_operator(request, pk):
  operator = GPSOperator.objects.get(id=pk)
  if request.method == 'POST':
    operator.delete()
    return redirect('gps_operator')
  context ={
    'operator': operator,
  }
  return render(request, 'records/delete_operator.html', context)

#  ---End of Operator and Vehicle CRUD---

# ---Start of Vehicle CRUD---
def vehicle(request):
  vehicle = Vehicle.objects.all()
  context = {
    'vehicle': vehicle,
  }
  return render(request, 'records/vehicle.html', context)

def add_vehicle(request):
  form = VehicleForm
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('vehicle')
  context = {
    'form': form,
  }
  return render(request, 'records/add_vehicle_form.html', context)

def update_vehicle(request, pk):
  vehicle = Vehicle.objects.get(id=pk)
  form = VehicleForm(instance=vehicle)
  if request.method == 'POST':
    form = VehicleForm(request.POST, instance=vehicle)
    if form.is_valid():
      form.save()
      return redirect('vehicle')
  context ={
    'form': form,
  }
  return render(request, 'records/add_vehicle_form.html', context)

def delete_vehicle(request, pk):
  vehicle = Vehicle.objects.get(id=pk)
  if request.method == 'POST':
    vehicle.delete()
    return redirect('vehicle')
  context ={
    'vehicle': vehicle,
  }
  return render(request, 'records/delete_vehicle.html', context)

# ---End of Vehicle CRUD---


def gps_records(request):
  gps_coordinate = GPSCoordinate.objects.all()
  context = {
    'gps_coordinate': gps_coordinate,
  }
  return render(request, 'records/gps_records.html', context)


def pollution_records(request):
  p_data = PollutionData.objects.all()
  context ={
    'p_data': p_data,
  }
  return render(request, 'records/pollution_records.html', context)


def about_us(request):
    return render(request, 'menu/about_us.html', {})

def user(request):
    return render(request, 'user/user.html', {})

def settings(request):
    return render(request, 'user/settings.html', {})

def contact_us(request):
    return render(request, 'menu/contact_us.html', {})

