!!! DIESE DATEI IST NUR EINE HILFE UM BEFEHLE ZU MERKEN UND IST KEINE ANLEITUNG
    FÜR DEN BETRIEB DER SEITE ODER ALS ANWEISUNG GEDACHT !!!

!!! WENN DU DEN DJANGO TOUROTIAL NICHT VERSTANDEN HAST,
    BIST DU HIER FALSCH !!!

//virtuelle Umgebung erstellen
python -m venv env

//virtuelle Umgebung aktivieren
"./env/Scripts/activate"
"./env/Scripts/deactivate"

//django install LTS
pip install "Django>=4.2,<4.3"
    //save the requirement.txt 
    pip freeze > requirement.txt
    // restore pip
    pip install -r requirement.txt


//Projekt starten
django-admin startproject website .

//applikation starten in cmd. IP kann in settings.py eingestellt werden
python manage.py runserver 

//interne serverweiterleitung nach Außen verfügbar
python manage.py runserver 0.0.0.0:8000

//appplattform generieren. muss in settings.py unter applikation eingetragen werden
python manage.py startapp "den Namen der App" 

// This command copies all static files from your apps to the STATIC_ROOT directory specified in your settings file.
python manage.py collectstatic

{//Models.py migrieren Step 1/2
python manage.py makemigrations

//SQL erstellen step 2/2
python manage.py migrate}

// --------------- ERROR PYTHON OR PIP NOT FOUND --------------------
1 "./env/Scripts/deactivate"
2 pip --version = true?
3 python --version = true?
4 python -m venv (choose new name) //dont delete or choose the existing env
5 ( python -m ) pip install -r requirement.txt = true?
6 "./(choose new name)/Scripts/activate" = true?
7 ( python -m ) pip freeze = true?
8 python manage.py runserver = true?
9 drink a beer
