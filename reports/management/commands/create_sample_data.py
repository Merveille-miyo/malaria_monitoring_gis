from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from accounts.models import User
from reports.models import MalariaCaseReport, Alert, Intervention
from gisdata.models import Neighborhood, RiskZone, HealthFacility

class Command(BaseCommand):
    help = 'Create sample data for the Malaria Monitoring System'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample users
        self.create_sample_users()
        
        # Create sample reports
        self.create_sample_reports()
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))

    def create_sample_users(self):
        """Create sample users for different roles"""
        users_data = [
            {'username': 'healthworker1', 'role': 'healthworker'},
            {'username': 'medofficer1', 'role': 'medofficer'},
            {'username': 'analyst1', 'role': 'analyst'},
            {'username': 'publicuser1', 'role': 'publicuser'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': f"{user_data['username']}@example.com",
                    'role': user_data['role'],
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')

    def create_sample_reports(self):
        """Create sample malaria case reports"""
        health_workers = User.objects.filter(role='healthworker')
        severities = ['low', 'medium', 'high', 'critical']
        
        for i in range(10):  # Create 10 sample reports
            reporter = random.choice(health_workers)
            severity = random.choice(severities)
            # Use random coordinates around Cameroon
            latitude = 6.6111 + random.uniform(-1, 1)
            longitude = 20.9394 + random.uniform(-1, 1)
            
            report = MalariaCaseReport.objects.create(
                reporter=reporter,
                latitude=latitude,
                longitude=longitude,
                symptoms=f'Sample symptoms for report {i+1}',
                severity=severity,
                validated=random.choice([True, False]),
            )
            
            self.stdout.write(f'Created report: {report.id}')

    def create_sample_alerts(self):
        """Create sample alerts"""
        med_officers = User.objects.filter(role='medofficer')
        alert_data = [
            {
                'title': 'High Malaria Activity Detected',
                'message': 'Multiple cases reported in Central District. Increased surveillance recommended.',
                'level': 'high'
            },
            {
                'title': 'Critical Outbreak Alert',
                'message': 'Confirmed malaria outbreak in Rural Village. Immediate intervention required.',
                'level': 'critical'
            },
            {
                'title': 'Moderate Risk Increase',
                'message': 'Rising case numbers in Urban Center. Monitor closely.',
                'level': 'medium'
            },
        ]
        
        for alert_info in alert_data:
            created_by = random.choice(med_officers)
            location = Point(20.9394, 6.6111)  # Center of Cameroon
            
            alert = Alert.objects.create(
                title=alert_info['title'],
                message=alert_info['message'],
                level=alert_info['level'],
                location=location,
                created_by=created_by,
                is_active=True,
            )
            
            self.stdout.write(f'Created alert: {alert.title}')

    def create_sample_interventions(self):
        """Create sample interventions"""
        med_officers = User.objects.filter(role='medofficer')
        intervention_types = ['spraying', 'nets', 'medication', 'education', 'testing']
        statuses = ['planned', 'in_progress', 'completed']
        
        intervention_data = [
            {
                'title': 'Mosquito Spraying Campaign',
                'description': 'Comprehensive spraying program in high-risk areas',
                'intervention_type': 'spraying',
                'status': 'in_progress'
            },
            {
                'title': 'Bed Net Distribution',
                'description': 'Distribute insecticide-treated bed nets to vulnerable populations',
                'intervention_type': 'nets',
                'status': 'planned'
            },
            {
                'title': 'Public Health Education',
                'description': 'Community awareness campaign about malaria prevention',
                'intervention_type': 'education',
                'status': 'completed'
            },
        ]
        
        for intervention_info in intervention_data:
            created_by = random.choice(med_officers)
            location = Point(20.9394, 6.6111)  # Center of Cameroon
            planned_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            
            intervention = Intervention.objects.create(
                title=intervention_info['title'],
                description=intervention_info['description'],
                intervention_type=intervention_info['intervention_type'],
                location=location,
                planned_date=planned_date,
                status=intervention_info['status'],
                created_by=created_by,
                resources_needed='Staff, equipment, and materials',
                budget=random.randint(5000, 50000),
            )
            
            self.stdout.write(f'Created intervention: {intervention.title}') 