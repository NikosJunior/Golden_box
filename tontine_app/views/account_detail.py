from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
def account_detail(request,pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    accounts = Account.objects.filter(user = user)
    return render(request, 'tontine_app/account_detail.html', {'accounts':accounts})