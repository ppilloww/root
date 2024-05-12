//virtuelle Umgebung erstellen
python -m venv env

//virtuelle Umgebung aktivieren
"./env/Scripts/activate"

//Projekt starten
django-admin startproject bbq_gmbh .

//applikation starten in cmd. IP kann in settings.py eingestellt werden
python manage.py runserver 

//interne serverweiterleitung nach Außen verfügbar
python manage.py runserver 0.0.0.0:8000

//appplattform generieren. muss in settings.py unter applikation eingetragen werden
python manage.py startapp bbq_gmbh_app"den Namen der App" 

// This command copies all static files from your apps to the STATIC_ROOT directory specified in your settings file.
python manage.py collectstatic

//Models.py migrieren Step 1/2
python manage.py makemigrations

//SQL erstellen step 2/2
python manage.py migrate

//migrtions error 1/2
python manage.py makemigrations bbq_gmbh_app --empty
2/2
python manage.py migrate

//  password hashing and salting.  {% csrf_token %} inside your form
This is a security measure that protects against cross-site request forgery attacks. Django will not process a form submission without a valid CSRF token.

