from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *


def index(request):
  return render(request, 'menu/home.html', {})

def home(request):
  return render(request, 'menu/home.html', {})

def dashboard(request):
  return render(request, 'menu/dashboard.html', {})

def traffic_management(request):
  coordinates = GPSCoordinate.objects.all()
  context = {
     'coordinates': coordinates,
  }
  return render(request, 'menu/traffic_management.html', context)

def traffic_management2(request):
  return render(request, 'menu/traffic_management2.html', {})

def pollution_management(request):
  
  return render(request, 'menu/pollution_management.html', {})

def devices(request):
  return render(request, 'menu/devices.html', {})

def gps_device(request, pk):
  
  return render(request, 'records/gps_device.html', {})

def pollution_device(request, pk):
  
  return render(request, 'records/pd_device.html', {})


def add_gps(request):

  return render(request, 'records/add_gps_form.html', {})

def update_gps(request, pk):
  
  return render(request, 'records/add_gps_form.html', {})

def gps_operator(request):
  
  return render(request, 'menu/gps_operator.html', {})

def gps_records(request):
  return render(request, 'records/gps_records.html', {})


def pollution_records(request):
  return render(request, 'records/pollution_records.html', {})


def about_us(request):
    return render(request, 'menu/about_us.html', {})

def user(request):
    return render(request, 'user/user.html', {})

def settings(request):
    return render(request, 'user/settings.html', {})

def contact_us(request):
    return render(request, 'menu/contact_us.html', {})

