from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account,Transaction
from django.contrib import messages

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
            
        if(request.POST.get('pk_cancel')):
            pk = request.POST.get('pk_cancel')
            transaction = Transaction.objects.get(pk = pk)
            transaction.status = 'canceled'
            transaction.save() 





            

        
    return render(request, 'tontine_app/withdraw_validation.html', {'transactions':transactions})