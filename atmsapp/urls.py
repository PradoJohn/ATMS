from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
<<<<<<< HEAD
=======
    path('gps_records/', views.gps_records, name = 'gps_records'),
    path('location/', views.location, name = 'location'),
    path('add_location/', views.add_location, name = 'add_location'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
    path('home/',views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('traffic_management/', views.traffic_management, name = 'traffic_management'),
    path('traffic_management2/', views.traffic_management2, name = 'traffic_management2'),
    path('pollution_management/', views.pollution_management, name = 'pollution_management'),
    path('devices/', views.devices, name = 'devices'),
<<<<<<< HEAD
    path('gps_device/<str:pk>/', views.gps_device, name = 'gps'),
    path('pollution_device/<str:pk>/', views.pollution_device, name = 'p_device'),
    path('add_gps/', views.add_gps, name = 'add_gps'),
    path('update_gps/', views.update_gps, name = 'update_gps'),
    path('gps_operator/', views.gps_operator, name = 'gps_operator'),
    path('vehicle/', views.vehicle, name = 'vehicle'),
    path('gps_records/', views.gps_records, name = 'gps_records'),
    path('pollution_records/', views.pollution_records, name = 'pollution_records'),
    path('user/', views.user, name = 'user'),
    path('settings/', views.settings, name = 'settings'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('about_us/', views.about_us, name = 'about_us'),
=======
    path('gps_device/<str:pk>/', views.gps_device, name = 'gps_device'),
    path('pollution_device/<str:pk>/', views.pollution_device, name = 'pollution_device'),
    path('pollution_records/', views.pollution_records, name = 'pollution_records'),
    path('gps_handlers/', views.gps_handlers, name = 'gps_handlers'),
    path('user/', views.user, name = 'user'),
    path('settings/', views.settings, name = 'settings'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('add_location/addrecord/', views.addrecord, name='addrecord'),
>>>>>>> 0231ed4ec1bd231adbb02455cd6d61efe0e65cea
    

]