from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('new/', views.report_create, name='report_create'),
    path('myreports/', views.report_list, name='report_list'),
]
