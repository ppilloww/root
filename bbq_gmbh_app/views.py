from django.shortcuts import render
from django.http import JsonResponse
from datetime import date, datetime
import holidays
from .models import Adresse, Mitarbeiter, Abteilungsleiter, Abteilung
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'indexEn.html')

def signin(request):
    return render(request, 'signinEn.html')

def home(request):
    return render(request, 'homeEnHr.html')

def changePassword(request):
    return render(request, 'pwEn.html')

def employeeManagement(request):
    return render(request, 'employeeManagementEn.html')

def profile(request):
    return render(request, 'profileEn.html')

######################################### authentcation #########################################

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'inactive'})
        else:
            return JsonResponse({'status': 'invalid'})

######################################### authentcation #########################################

######################################### Logics #########################################

# checkig publick holidays
def checkHolidays(request):
    today = date.today()
    de_holidays = holidays.Germany(prov='BW')
    is_public_holiday = today in de_holidays
    is_sunday = today.weekday() == 6 #6 = sunday
    context = {'non_working_day': False } #is_public_holiday or is_sunday
    return JsonResponse(context)

######################################### Logics #########################################

######################################### Database operations #########################################

def create_mitarbeiter(strasse, hausnummer, stadt, plz, land, vorname, nachname, email, geburtsdatum, position, gehalt, hr_tag, passwort, admin_tag, urlaubstage, wochenstundensatz, ueberstunden, geschlecht, quartalueberstunden, jahresueberstunden, abteilungsleiter_vorname, abteilungsleiter_nachname, abteilungsleiter_email,abteilungsname):
    # Überprüfen, ob die Adresse existiert
    try:
        adresse = Adresse.objects.get(strasse=strasse, hausnummer=hausnummer, stadt=stadt, plz=plz, land=land)
    except Adresse.DoesNotExist:
        # Wenn die Adresse nicht existiert, erstellen Sie eine neue
        adresse = Adresse.objects.create(strasse=strasse, hausnummer=hausnummer, stadt=stadt, plz=plz, land=land)
        
    try:
        abteilungsleiter = Abteilungsleiter.objects.get(vorname=abteilungsleiter_vorname, nachname=abteilungsleiter_nachname, email=abteilungsleiter_email)
    except Adresse.DoesNotExist:
        # Wenn die Adresse nicht existiert, erstellen Sie eine neue
        abteilungsleiter = Abteilungsleiter.objects.create(vorname=abteilungsleiter_vorname, nachname=abteilungsleiter_nachname, email=abteilungsleiter_email)
         
           
    try:
        abteilung = Abteilung.objects.get(abteilungsname=abteilungsname)
    except Adresse.DoesNotExist:
        abteilung = Abteilung.objects.create(abteilungsname=abteilungsname, abteilungsleiter=abteilungsleiter)
      
         

    # Überprüfen, ob der Mitarbeiter existiert
    try:
        mitarbeiter = Mitarbeiter.objects.get(vorname=vorname, nachname=nachname, email=email)
        
    except Mitarbeiter.DoesNotExist:
        # Wenn der Mitarbeiter nicht existiert, erstellen Sie einen neuen
        mitarbeiter = Mitarbeiter.objects.create(
            adresse=adresse,
            vorname=vorname,
            nachname=nachname,
            email=email,
            geburtsdatum=datetime.strptime(geburtsdatum, '%Y-%m-%d').date(),
            position=position,
            gehalt=gehalt,
            hr_tag=hr_tag,
            passwort=passwort,
            admin_tag=admin_tag,
            urlaubstage=urlaubstage,
            wochenstundensatz=wochenstundensatz,
            ueberstunden=ueberstunden,
            geschlecht=geschlecht,
            quartalueberstunden=quartalueberstunden,
            jahresueberstunden=jahresueberstunden
    )
        
def mitarbeiter_loeschen(mitarbeiter_id=None, vorname=None, nachname=None):
    if mitarbeiter_id:
        filter_args = {'id': mitarbeiter_id}
    elif vorname and nachname:
        filter_args = {'vorname': vorname, 'nachname': nachname}
    else:
        return False, "Bitte geben Sie eine Mitarbeiter-ID oder Vor- und Nachnamen an."

    try:
        mitarbeiter = Mitarbeiter.objects.get(**filter_args)
        abteilungen_leitung = Abteilung.objects.filter(abteilungsleiter=mitarbeiter)

        # Setze den Abteilungsleiter der betroffenen Abteilungen auf NULL
        for abteilung in abteilungen_leitung:
            abteilung.abteilungsleiter = None
            abteilung.save()

        # Lösche die Adresse des Mitarbeiters
        mitarbeiter.adresse.delete()
        # Lösche alle Arbeitsstunden des Mitarbeiters
        mitarbeiter.arbeitsstunden.all().delete()
        # Lösche alle Urlaube des Mitarbeiters
        mitarbeiter.urlaube.all().delete()
        # Lösche den Mitarbeiter selbst
        mitarbeiter.delete()

        return True, f"Mitarbeiter {mitarbeiter} und alle zugehörigen Daten wurden erfolgreich gelöscht."
    except Mitarbeiter.DoesNotExist:
        return False, f"Mitarbeiter mit den angegebenen Daten wurde nicht gefunden."
    except Exception as e:
        return False, f"Fehler beim Löschen des Mitarbeiters: {str(e)}"




def mitarbeiter_aktualisieren(mitarbeiter_id):
    try:
        mitarbeiter = Mitarbeiter.objects.get(id=mitarbeiter_id)
        adresse = mitarbeiter.adresse
        
        neue_daten = erstelle_neue_daten_mitarbeiter_und_adresse(mitarbeiter_id)
        
        if neue_daten:
            mitarbeiter.update(**neue_daten)
            adresse.update(**neue_daten)

            return True, f"Mitarbeiter {mitarbeiter_id} und Adresse wurden erfolgreich aktualisiert."
        else:
            return False, f"Mitarbeiter mit der ID {mitarbeiter_id} wurde nicht gefunden."
    except Exception as e:
        return False, f"Fehler beim Aktualisieren des Mitarbeiters und der Adresse: {str(e)}"




def erstelle_neue_daten_mitarbeiter_und_adresse(mitarbeiter_id, **kwargs):
    try:
        mitarbeiter = Mitarbeiter.objects.get(id=mitarbeiter_id)
        adresse = mitarbeiter.adresse

        # Extrahiere die Feldnamen der Mitarbeiter-Tabelle
        mitarbeiter_feldnamen = [feld.name for feld in Mitarbeiter._meta.get_fields() if feld.name != 'id']

        # Extrahiere die Feldnamen der Adresse-Tabelle
        adresse_feldnamen = [feld.name for feld in Adresse._meta.get_fields() if feld.name != 'id']

        # Kombiniere die Feldnamen beider Tabellen
        alle_feldnamen = mitarbeiter_feldnamen + adresse_feldnamen

        # Erstelle das Wörterbuch mit allen Feldern und ihren aktuellen Werten
        neue_daten = {feld: getattr(mitarbeiter, feld) for feld in alle_feldnamen}

        return neue_daten
    except Mitarbeiter.DoesNotExist:
        return None


######################################### Database operations #########################################
