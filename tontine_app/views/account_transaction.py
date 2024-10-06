from django.shortcuts import render
from ..models import Transaction, Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
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