from django.urls import path
from . import views

urlpatterns = [
    # Sidebar Navigation patterns
    path('', views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('traffic_management/', views.traffic_management, name = 'traffic_management'),
    path('traffic_management2/', views.traffic_management2, name = 'traffic_management2'),
    path('pollution_management/', views.pollution_management, name = 'pollution_management'),

    # Devices CRUD url patterns
    path('devices/', views.devices, name = 'devices'),
    path('gps_device/<str:pk>/', views.gps_device, name = 'gps'),
    path('pollution_device/<str:pk>/', views.pollution_device, name = 'p_device'),
    path('add_gps/', views.add_gps, name = 'add_gps'),
    path('update_gps/<str:pk>/', views.update_gps, name = 'update_gps'),
    path('delete_gps/<str:pk>/', views.delete_gps, name = 'delete_gps'),


    # Operator & Vehicle CRUD url patters
    path('gps_operator/', views.gps_operator, name = 'gps_operator'),
    path('vehicle/', views.vehicle, name = 'vehicle'),
    path('add_operator/', views.add_operator, name = 'add_operator'),
    path('add_vehicle/', views.add_vehicle, name = 'add_vehicle'),
    path('update_operator/<str:pk>/', views.update_operator, name = 'update_operator'),
    path('update_vehicle/<str:pk>/', views.update_vehicle, name = 'update_vehicle'),
    path('delete_operator/<str:pk>/', views.delete_operator, name = 'delete_operator'),
    path('delete_vehicle/<str:pk>/', views.delete_vehicle, name = 'delete_vehicle'),


    # Add Realtime Data Sample
    path('add_coordinate/', views.add_coordinate, name = 'add_coordinate'),


    path('gps_records/', views.gps_records, name = 'gps_records'),
    path('pollution_records/', views.pollution_records, name = 'pollution_records'),
    path('user/', views.user, name = 'user'),
    path('settings/', views.settings, name = 'settings'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('about_us/', views.about_us, name = 'about_us'),
    

]