from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bbq_gmbh_app/index.html')

def signin(request):
    return render(request, 'bbq_gmbh_app/signin.html')