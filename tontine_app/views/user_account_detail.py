from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account, Transaction
from django.contrib.auth.decorators import login_required

@login_required
def user_account_detail(request,pk):
    account = Account.objects.get(pk = pk)
    transactions = Transaction.objects.filter(account= account).order_by('-transaction_date')
    return render(request, 'tontine_app/user_account_detail.html',  {"transactions": transactions })