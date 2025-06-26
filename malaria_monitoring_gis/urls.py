from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('reports/', include('reports.urls')),
    path('gisdata/', include('gisdata.urls')),
    path('', include('dashboard.urls')),
]
