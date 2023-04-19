from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def dashboard(request):
    return render(request, 'menu/dashboard.html', {})

def index(request):
    return render(request, 'menu/home.html', {})
    
def traffic_management(request):
  gps_information = GPSInformation.objects.all()
  context = {
     'gps_information': gps_information,
  }
  return render(request, 'menu/traffic_management.html', context)

def traffic_management2(request):
    return render(request, 'menu/traffic_management2.html', {})

def pollution_management(request):
  pollution_information = AirPollutionInformation.objects.all()
  pollution_detector = PollutionDetector.objects.all()
  context = {
    'pollution_information': pollution_information,
    'pollution_detector' : pollution_detector,
    }
  return render(request, 'menu/pollution_management.html', context)

def home(request):
    return render(request, 'menu/home.html', {})

def about(request):
    return render(request, 'menu/about_us.html', {})

def user(request):
    return render(request, 'user/user.html', {})

def settings(request):
    return render(request, 'user/settings.html', {})

def contact(request):
    return render(request, 'menu/contact_us.html', {})

def devices(request):
  gps_device = GPSDevice.objects.all()
  pollution_device = PollutionDetector.objects.all()

  total_gps_devices = gps_device.count()
  total_pollution_devices = pollution_device.count()
  deployed_gps = gps_device.filter(status='Deployed').count()
  deployed__pollution_device = pollution_device.filter(status='Deployed').count()
  context = {
    'gps_device': gps_device,
    'pollution_device': pollution_device,
    'total_gps_devices': total_gps_devices,
    'total_pollution_devices': total_pollution_devices,
    'deployed_gps': deployed_gps,
    'deployed__pollution_device': deployed__pollution_device,

  }
  return render(request, 'menu/devices.html', context)


def gps_device(request, pk):
  gps_device = GPSDevice.objects.get(id=pk)
  gps_information = gps_device.gpsinformation_set.all()
  context = {
     'gps_device': gps_device,
     'gps_information': gps_information,
  }
  return render(request, 'devices/gps_device.html', context)

def pollution_device(request, pk):
  pollution_device = PollutionDetector.objects.get(id=pk)
  pd_information = pollution_device.airpollutioninformation_set.all()
  context = {
     'pollution_device': pollution_device,
     'pd_information': pd_information,
  }
  return render(request, 'devices/pollution_device.html', context)


def gps_handlers(request):
  gps_handlers = GPSHolder.objects.all()
  vehicles = GPSVehicle.objects.all()
  context = {
      'gps_handlers': gps_handlers,
      'vehicles': vehicles
  }
  return render(request, 'menu/gps_handlers.html', context)

def pollution_records(request):
  pollution_information = AirPollutionInformation.objects.all()
  pollution_detector = PollutionDetector.objects.all()
  context = {
    'pollution_information': pollution_information,
    'pollution_detector' : pollution_detector,
    }
  return render(request, 'records/pollution_records.html', context)

def gps_records(request):
  gps_information = GPSInformation.objects.all()
  gps_device = GPSDevice.objects.all()
  context = {
      'gps_information' : gps_information,
      'gps_device' : gps_device,
  }
  return render(request, 'records/gps_records.html', context)
    

def location(request):
    location = Location.objects.all().values()
    template = loader.get_template('records/location.html')
    context = {
    'location': location,
  }
    return HttpResponse(template.render(context, request))

def add_location(request):
    location = Location.objects.all().values()
    template = loader.get_template('records/add_location.html')
    context = {
    'location': location,
  }
    return HttpResponse(template.render(context, request))

def addrecord(request):
  x = request.POST['road']
  y = request.POST['type']
  road = Road(road_name=x, road_type=y)
  road.save()
  return HttpResponseRedirect(reverse('add_location'))


def road(request):
  road = Road.objects.all().values()
  template = loader.get_template('records/road.html')
  context = {
    'road': road,
  }
  return HttpResponse(template.render(context, request))

