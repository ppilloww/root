!!! DIESE DATEI IST NUR EINE HILFE UM BEFEHLE ZU MERKEN UND IST KEINE ANLEITUNG
    FÜR DEN BETRIEB DER SEITE ODER ALS ANWEISUNG GEDACHT !!!

!!! WENN DU DEN DJANGO TOUROTIAL NICHT VERSTANDEN HAST,
    BIST DU HIER FALSCH !!!

    !!! ACHTUNG ... Lege für deinen PC eine neu virtuelle Umgebung an und installiere requirements.txt in deiner virtuellen Umgebung !!!

//virtuelle Umgebung erstellen
python -m venv env(_"küezel"_"nb oder pc")

//virtuelle Umgebung aktivieren
"./env/Scripts/activate"
"./env_nb/Scripts/activate"
"./env_pz_nb/Scripts/activate"


"./env/Scripts/deactivate"
"./env_nb/Scripts/deactivate"
"./env_pz_nb/Scripts/deactivate"


//django install LTS
pip install "Django>=4.2,<4.3"
    //save the requirements.txt 
    pip freeze > requirements.txt
    // restore pip
    pip install -r requirements.txt


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
5 "./(choose new name)/Scripts/activate" = true?
6 ( python -m ) pip install -r requirement.txt = true?
7 ( python -m ) pip freeze = true?
8 python manage.py runserver = true?
9 drink a beer
