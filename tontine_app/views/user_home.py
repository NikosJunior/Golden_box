from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account
from django.contrib.auth.decorators import login_required

@login_required
def user_home(request,pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    accounts = Account.objects.filter(user = user)
    return render(request, 'tontine_app/user_home.html', {'accounts':accounts})