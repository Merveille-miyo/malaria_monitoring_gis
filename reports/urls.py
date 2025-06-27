from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('new/', views.report_create, name='report_create'),
    path('myreports/', views.report_list, name='report_list'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/<int:pk>/validate/', views.report_validate, name='report_validate'),
]
