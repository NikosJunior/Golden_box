from django.shortcuts import render
from django.contrib.auth import get_user_model
from ..models import Account
from django.contrib import messages


from django.contrib.auth.decorators import user_passes_test

from ..models import Account

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
def add_account(request,pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    if(request.method == 'POST'):
        payment = request.POST.get('payment')
        account = Account.objects.create(
            user = user,
            payment = payment,
        )

        messages.info(request, 'compte créé avec succès')
    return render(request, 'tontine_app/add_account.html', {'user':user})