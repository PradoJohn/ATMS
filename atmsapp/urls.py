from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gps_records/', views.gps_records, name = 'gps_records'),
    path('location/', views.location, name = 'location'),
    path('add_location/', views.add_location, name = 'add_location'),
    path('road/', views.road, name = 'road'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('home/',views.home, name = 'home'),
    path('traffic_management/', views.traffic_management, name = 'traffic_management'),
    path('traffic_management2/', views.traffic_management2, name = 'traffic_management2'),
    path('pollution_management/', views.pollution_management, name = 'pollution_management'),
    path('devices/', views.devices, name = 'devices'),
    path('pollution_records/', views.pollution_records, name = 'pollution_records'),
    path('gps_handlers/', views.gps_handlers, name = 'gps_handlers'),
    path('user/', views.user, name = 'user'),
    path('settings/', views.settings, name = 'settings'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('add_location/addrecord/', views.addrecord, name='addrecord'),
    
    
]