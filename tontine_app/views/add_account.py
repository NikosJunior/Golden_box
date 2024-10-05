from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account
from django.contrib import messages

def add_account(request,pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    if(request.method == 'POST'):
        payment = request.POST.get('payment')
        account = Account.objects.create(
            user = user,
            payment = payment,
        )

        messages.info(request, 'compte créé avec succès')
    return render(request, 'tontine_app/add_account.html', {'user':user})