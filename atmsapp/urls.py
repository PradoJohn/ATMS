from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_records/', views.all_records, name = 'all_records'),
    path('location/', views.location, name = 'location'),
    path('add_location/', views.add_location, name = 'add_location'),
    path('road/', views.road, name = 'road'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('home/',views.home, name = 'home'),
    path('gps_sensors/', views.gps_sensors, name = 'gps_sensors'),
    path('air_quality/', views.air_quality, name = 'air_quality'),
    path('all_records/delete/<int:id>', views.delete, name='delete'),
    path('user/', views.user, name = 'user'),
    path('help/', views.help, name = 'help'),
    path('add_location/addrecord/', views.addrecord, name='addrecord'),
    path('book/<int:book_id>', views.book_by_id, name = 'book_by_id'),
    
]