from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from ..models import Account,Transaction
from datetime import timedelta, datetime
from django.contrib import messages


def deposit(request, pk):

    User = get_user_model()
    user = User.objects.get(pk = pk)
    accounts = Account.objects.filter(user = user)
    if (request.method == "POST"):
        if (request.POST.get("amount")):
            amount = request.POST.get("amount")
            pk_account = request.POST.get("account")
            date_str = request.POST.get("date")
            account = Account.objects.get(pk=pk_account)
            if (date_str== "") :
                messages.error(request, f"veuillez entrer la date de paie si elle n'est pas déja utilisé")
                return render(request, 'tontine_app/deposit.html', {"accounts" :accounts })
            
            if (amount== "") :
                messages.error(request, f"veuillez entrer le montant de paie")
                return render(request, 'tontine_app/deposit.html', {"accounts" :accounts })

            date_ = datetime.strptime(date_str, '%Y-%m-%d').date()

            if(int(amount)/account.payment == 1):
                try:
                    Transaction.objects.create(
                        customer = user,
                        account = account,
                        transaction_date = date_,
                        amount = amount,
                    )
                    account.balance= account.balance + account.payment
                    account.save()
                    messages.success(request, 'Enregistrement fait avec succès')

                except Exception as e:
                    messages.error(request, f"Erreur lors de l'enregistrement de la transaction : veuillez bien vérifier la date de paie si elle n'est pas déja utilisé")

            if(int(amount)/account.payment > 1):
                try:
                    for i in range(int(amount) // account.payment):
                
                        Transaction.objects.create(
                            customer = user,
                            account = account,
                            transaction_date = date_,
                            amount = account.payment,
                        )
                        account.balance+= account.payment

                        date_ = date_ + timedelta(days=1)
                
                        account.save()

                    messages.success(request, f'Dépot de {amount} effectué avec succès fait ')

                except Exception as e:
                    messages.error(request, f"Erreur lors de l'enregistrement de la transaction : veuillez bien vérifier la date de paie si elle n'est pas déja utilisé")
        
    return render(request, 'tontine_app/deposit.html', {"accounts" :accounts })