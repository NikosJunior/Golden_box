from django.shortcuts import render

def home(request):
    return render(request, 'tontine_app/home.html')