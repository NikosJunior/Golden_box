from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager')

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
def accounts(request):
    User = get_user_model()
    users = User.objects.filter(user_type = 'customer').order_by("-date_joined")
    return render(request, 'tontine_app/accounts.html', {"users": users})