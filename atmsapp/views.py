from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
<<<<<<< HEAD
from .forms import *
=======
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea


def index(request):
<<<<<<< HEAD
  return render(request, 'menu/home.html', {})
=======
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
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea

def home(request):
  return render(request, 'menu/home.html', {})

def dashboard(request):
  return render(request, 'menu/dashboard.html', {})

def traffic_management(request):
  coordinates = GPSCoordinate.objects.all()
  gps_device = GPSDevice.objects.filter(status='Malfunctioned')
  operator = GPSOperator.objects.all()
  context = {
     'coordinates': coordinates,
     'gps_device': gps_device,
     'operator': operator,
  }
  return render(request, 'menu/traffic_management.html', context)

def traffic_management2(request):
  gps_device = GPSDevice.objects.all()
  context = {
    'gps_device': gps_device,
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


def add_gps(request):

  return render(request, 'records/add_gps_form.html', {})

def update_gps(request, pk):
  
  return render(request, 'records/add_gps_form.html', {})

def gps_operator(request):
  operator = GPSOperator.objects.all()
  context = {
    'operator': operator,
  }
  return render(request, 'records/gps_operator.html', context)

def vehicle(request):
  vehicle = Vehicle.objects.all()
  context = {
    'vehicle': vehicle,
  }
  return render(request, 'records/vehicle.html', context)

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

<<<<<<< HEAD
=======
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

>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
