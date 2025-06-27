from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('trends/', views.trends, name='trends'),
    path('heatmap/', views.heatmap, name='heatmap'),
    path('alerts/', views.alerts, name='alerts'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
