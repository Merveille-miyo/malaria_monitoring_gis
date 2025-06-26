The task is to build a malaria monitoring Geographic information system that integrates spatial data like maps , with a health data to track , analyse and predict malaria outbreaks in Cameroon, it allows authorities to visualize neighborhoods with high risk of malaria outbreak
What happens in the background is that health workers can authenticate in the system and report malaria cases in particular areas in Cameroon,use web form to enter details,triggers alerts or notification , then a map of cameroon that can be zoomed in and out will show areas infected / where there is a likelihood of outbreak like you can add a red region on the map
This will allow to identify potential outbreaks , enhanced surveillance and community engagement to limit malaria in particular areas,a System Administrator	- Sets up and configures the system- Manages users and access rights- Updates GIS map layers- Performs system maintenance
Health Worker	- Submits malaria case data (location, symptoms, severity)- Uses a web form to enter details- Triggers alerts or notifications upon submission
Medical Officer (Admin Role)	- Oversees all submitted data- Validates reports from health workers- Views neighborhood-level dashboards- Makes intervention decisions and resource dispatching
Health Analyst	- Analyzes case data trends- Generates reports, heatmaps, and graphs- Identifies high-risk zones using GIS tools- Informs medical officers for further action
Public User	- Views interactive malaria maps- Sees outbreak alerts and statistics- Receives risk-level information for neighborhoods- May sign up for notifications (email/SMS)

the user interface is modern and reflects health , protection and resilience
Malaria Monitoring GIS System (Django)

How to Run:

1. Ensure Python 3.10+ is installed
2. Install PostgreSQL and PostGIS (for GeoDjango)
3. Navigate to the project folder:
   cd malaria_monitoring_gis

4. Create virtual environment:
   python -m venv env
   source env/bin/activate  (Linux/macOS)
   env\Scripts\activate   (Windows)

5. Install dependencies:
   pip install -r requirements.txt

6. Set up the database (PostgreSQL + PostGIS):
   - Create a database 'malaria_db'
   - Enable PostGIS extension

7. Configure 'malaria_monitoring_gis/settings.py' with your DB credentials

8. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

9. Create superuser:
   python manage.py createsuperuser

10. Run the server:
    python manage.py runserver

11. Open http://127.0.0.1:8000 in your browser

Modules:
- accounts: user roles and auth
- reports: malaria case reports
- gisdata: neighborhood map and risk zones
- dashboard: charts, analytics
