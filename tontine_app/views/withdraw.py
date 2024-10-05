from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account,Transaction
from django.contrib import messages

def withdraw(request, pk):

    User = get_user_model()
    user = User.objects.get(pk = pk)
    accounts = Account.objects.filter(user = user)
    if (request.method == "POST"):
        if (request.POST.get("amount")):
            amount = request.POST.get("amount")
            pk_account = request.POST.get("account")
            account = Account.objects.get(pk=pk_account)
            if( int(amount) < account.balance ):
                Transaction.objects.create(
                    customer = user,
                    account = account,
                    amount = int(amount),
                    transaction_type = 'withdraw',
                )
                messages.success(request, "Demande de retrait créé avec succès")

            
            else:
                messages.error(request, "balance insuffisant")





            

        
    return render(request, 'tontine_app/withdraw.html', {"accounts" :accounts })