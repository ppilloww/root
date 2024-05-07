from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from datetime import date, datetime
import holidays
from bbq_gmbh_app.models import Adresse, Mitarbeiter, Abteilungsleiter, Abteilung
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
    user_view_response = user_view(request)
    if 'error' in user_view_response:
        return JsonResponse({'error': 'User not found'}, status=404)
    employees = user_view_response['employees']
    return render(request, 'employeeManagementEn.html', {'employees': employees})

def profile(request):
    return render(request, 'profileEn.html')

def addUser(request):
    return render(request, 'addUser.html')



######################################### authentcation #########################################

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Authenticate user
#         user = authenticate(request, email=email, passwort=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 request.session['user_role'] = user.role
#                 return JsonResponse({'status': 'success', 'user_role': user.role}, status=200)
#             else:
#                 return JsonResponse({'status': 'inactive'}, status=401)
#         else:
#             return JsonResponse({'status': 'invalid'}, status=401)

#     # Handle GET request (if needed)
#     return render(request, "signinEn.html")



def login_view(request):
    if request.method == 'POST':
        # Get email and password from POST data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Perform authentication
        try:
            user = Mitarbeiter.objects.get(email=email, password=password)
            if user:
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role
                # print("User ID:", request.session['user_id'])
                # print("User role:", request.session['user_role'])
                # uno = Mitarbeiter.objects.get()
                # print(uno)
                return JsonResponse({'status': 'success'}, status=200)
        except Mitarbeiter.DoesNotExist:
            return JsonResponse({'status': 'invalid'}, status=401)

    return render(request, "signinEn.html")

def get_user_role(request):
    user_role = request.session.get('user_role', None)
    if user_role is None:
        return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'user_role': user_role})

# def log out and flush session
def logout_view(request):
    request.session.flush()
    return redirect('index')

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

# get all employees
def user_view(request):
    user_id = request.session.get('user_id', None)
    # print("User_view_id:", user_id)
    if user_id is not None:
        # print("User_view:", user_id)
        employees = Mitarbeiter.objects.all()
        # print(employees)
        # return render(request, "employeeManagementEn.html", {'employees': employees})
        return {'employees': employees}
    return JsonResponse({'error': 'User not found'}, status=404)

# get user information

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
