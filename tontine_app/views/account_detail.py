from django.shortcuts import render

def account_detail(request):
    return render(request, 'tontine_app/account_detail.html')