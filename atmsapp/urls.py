from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('traffic_management/', views.traffic_management, name = 'traffic_management'),
    path('traffic_management2/', views.traffic_management2, name = 'traffic_management2'),
    path('pollution_management/', views.pollution_management, name = 'pollution_management'),
    path('devices/', views.devices, name = 'devices'),
    path('gps_device/', views.gps_device, name = 'gps_device'),
    path('pollution_device/', views.pollution_device, name = 'pollution_device'),
    path('add_gps/', views.add_gps, name = 'add_gps'),
    path('update_gps/', views.update_gps, name = 'update_gps'),
    path('gps_operator/', views.gps_operator, name = 'gps_operator'),
    path('gps_records/', views.gps_records, name = 'gps_records'),
    path('pollution_records/', views.pollution_records, name = 'pollution_records'),
    path('user/', views.user, name = 'user'),
    path('settings/', views.settings, name = 'settings'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('about_us/', views.about_us, name = 'about_us'),
    
]