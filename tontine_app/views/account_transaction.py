from django.shortcuts import render
from ..models import Transaction, Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def account_transation(request, pk):
    account = Account.objects.get(pk = pk)
    transactions = Transaction.objects.filter(account= account).order_by('-transaction_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(transactions, 10)
    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)
    return render(request, 'tontine_app/account_transaction.html', {"transactions": transactions })