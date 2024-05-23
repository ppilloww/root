//virtuelle Umgebung erstellen
python -m venv env

//virtuelle Umgebung aktivieren
"./env/Scripts/activate"
"./env/Scripts/deactivate"

//django install LTS
pip install "Django>=4.2,<4.3"

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

{//Models.py migrieren Step 1/2
python manage.py makemigrations

//SQL erstellen step 2/2
python manage.py migrate}
