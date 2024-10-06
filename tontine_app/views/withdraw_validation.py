from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account,Transaction
from django.contrib import messages
import africastalking
from django.contrib.auth.decorators import user_passes_test

username='sandbox'
api_key='atsk_f5cae138bf6dda35d3247babaf5ece2de127ca760bebb39b7dd06a923353debf391d39b0'

africastalking.initialize(username, api_key)
sms = africastalking.SMS

def is_admin(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.is_staff)

admin_required = user_passes_test(is_admin)

@admin_required
def withdraw_validation(request):
    transactions = Transaction.objects.filter(transaction_type = 'withdraw', status ='pending')
    if(request.method == 'POST'):
        if(request.POST.get('pk_valid')):
            pk = request.POST.get('pk_valid')
            transaction = Transaction.objects.get(pk = pk)
            amount = transaction.amount
            account = transaction.account
            account.balance= account.balance - amount
            account.save()
            transaction.status = 'done'
            transaction.save()
            recipients = ["+22961021564"] 
            message = f'Retrait de {amount} effectué avec succès fait. Nouveau solde:{account.balance} FCFA'
            sender = "3043"
            try:
                response = sms.send(message, recipients, sender)
                print(response)
            except Exception as e:
                print(f"Erreur d'envoi : {str(e)}")


            
        if(request.POST.get('pk_cancel')):
            pk = request.POST.get('pk_cancel')
            transaction = Transaction.objects.get(pk = pk)
            transaction.status = 'canceled'
            transaction.save()





            

        
    return render(request, 'tontine_app/withdraw_validation.html', {'transactions':transactions})