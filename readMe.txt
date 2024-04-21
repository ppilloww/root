//Projekt starten
django-admin startproject bbq_gmbh .

//applikation starten in cmd. IP kann in settings.py eingestellt werden
python manage.py runserver 

//interne serverweiterleitung nach Außen verfügbar
python manage.py runserver 0.0.0.0:8000

//appplattform generieren. muss in settings.py unter applikation eingetragen werden
python manage.py startapp bbq_gmbh_app"den Namen der App" 