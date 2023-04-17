from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import *


def dashboard(request):
    return render(request, 'menu/dashboard.html', {})

def index(request):
    return render(request, 'menu/home.html', {})
    
def traffic_management(request):
    return render(request, 'menu/traffic_management.html', {})

def traffic_management2(request):
    return render(request, 'menu/traffic_management2.html', {})

def pollution_management(request):
  record = Record.objects.all().values()
  road = Road.objects.all().values()
  location = Location.objects.all().values()
  vehicle = Vehicle.objects.all().values()
  template = loader.get_template('menu/pollution_management.html')
  context = {
    'record': record,
    'road': road,
    'location': location,
    'vehicle': vehicle,
  }
  return HttpResponse(template.render(context, request))

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
    return render(request, 'menu/devices.html', {})

def gps_handlers(request):
    return render(request, 'menu/gps_handlers.html', {})

def pollution_records(request):
    return render(request, 'records/pollution_records.html', {})

def all_records(request):
  record = Record.objects.all().values()
  road = Road.objects.all().values()
  location = Location.objects.all().values()
  vehicle = Vehicle.objects.all().values()
  template = loader.get_template('records/all_records.html')
  context = {
    'record': record,
    'road': road,
    'location': location,
    'vehicle': vehicle,
  }
  return HttpResponse(template.render(context, request))
    

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book': book})


def delete(request, id):
  record = Record.objects.get(id=id)
  record.delete()
  return HttpResponseRedirect(reverse('all_records'))


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

