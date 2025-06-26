from django.urls import path
from . import views

app_name = 'gisdata'

urlpatterns = [
    path('map/', views.map_view, name='map'),
]
