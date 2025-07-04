# Malaria Monitoring GIS System - Setup Guide

## Overview
This Django-based Geographic Information System (GIS) is designed to track, analyze, and predict malaria outbreaks in Cameroon. It integrates spatial data with health information to provide comprehensive monitoring capabilities.

## Features

### User Roles and Capabilities

1. **Health Worker**
   - Submit malaria case reports with location, symptoms, and severity
   - View their own submitted reports
   - Automatic alert triggering for high-severity cases

2. **Medical Officer (Admin Role)**
   - View and validate submitted reports from health workers
   - Access neighborhood-level dashboards
   - Manage interventions and resource allocation
   - Create alerts and notifications

3. **Health Analyst**
   - Analyze case data trends
   - Generate graphs, heatmaps, and reports
   - Use GIS tools to identify high-risk zones
   - Access advanced analytics dashboard

4. **Public User**
   - View interactive malaria risk maps
   - Access outbreak alerts and statistics
   - Check risk levels by neighborhood
   - Subscribe to notifications

## Technical Requirements

- Python 3.10+
- PostgreSQL with PostGIS extension
- Django 5.2+
- GeoDjango (included with Django)

## Installation Steps

### 1. Clone and Setup Environment
```bash
cd malaria_monitoring_gis
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create PostgreSQL database with PostGIS
createdb malaria_db
psql malaria_db -c "CREATE EXTENSION postgis;"
```

### 3. Configure Settings
Edit `malaria_monitoring_gis/settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'malaria_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Create Sample Data (Optional)
```bash
python manage.py create_sample_data
```

### 7. Run Development Server
```bash
python manage.py runserver
```

## Default Users (if using sample data)

- **Health Worker**: `healthworker1` / `password123`
- **Medical Officer**: `medofficer1` / `password123`
- **Health Analyst**: `analyst1` / `password123`
- **Public User**: `publicuser1` / `password123`

## Key Features

### Interactive Maps
- Leaflet-based interactive maps
- Multiple layers: risk zones, neighborhoods, health facilities
- Real-time case plotting
- Heatmap visualization

### Analytics Dashboard
- Case statistics and trends
- Severity distribution analysis
- Monthly trend visualization
- Risk zone analysis

### Alert System
- Automatic alerts for high-severity cases
- Manual alert creation by medical officers
- Public alert dissemination

### Role-Based Access Control
- Secure user authentication
- Role-specific permissions
- Protected views and actions

## File Structure

```
malaria_monitoring_gis/
├── accounts/          # User management and authentication
├── reports/           # Case reports, alerts, interventions
├── gisdata/           # Geographic data models
├── dashboard/         # Analytics and dashboards
├── templates/         # HTML templates
├── static/           # Static files (CSS, JS, images)
└── malaria_monitoring_gis/  # Project settings
```

## API Endpoints

- `/` - Main dashboard
- `/accounts/login/` - User login
- `/accounts/register/` - User registration
- `/reports/new/` - Submit new case report
- `/reports/myreports/` - View reports
- `/gisdata/map/` - Interactive map
- `/dashboard/analytics/` - Analytics dashboard

## Contributing

1. Follow Django best practices
2. Use GeoDjango for spatial operations
3. Implement proper role-based permissions
4. Test all user workflows
5. Document new features

## Support

For technical support or questions, please refer to the Django documentation and GeoDjango guides.
