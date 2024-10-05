from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account

def account_detail(request,pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    accounts = Account.objects.filter(user = user)
    return render(request, 'tontine_app/account_detail.html', {'accounts':accounts})