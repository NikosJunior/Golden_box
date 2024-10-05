from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account, Transaction
from django.db.models import Sum

def home(request):
    User = get_user_model()
    total_users = User.objects.count()
    total_balance = Account.objects.aggregate(Sum('balance'))['balance__sum']
    total_transactions_unvalid = Transaction.objects.filter(transaction_type = 'withdraw', status ='pending').count()
    context = {
        'total_users': total_users, 
        'total_balance': total_balance,
        'total_transactions_unvalid':total_transactions_unvalid 
        }
    return render(request, 'tontine_app/home.html', context)