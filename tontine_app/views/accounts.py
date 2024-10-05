from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or  user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
def accounts(request):
    User = get_user_model()
    search=request.GET.get('search')
    users = User.objects.filter(user_type = 'customer').order_by("-date_joined")
    if search:
        users = User.objects.filter(
            Q(last_name__icontains=search) |
            Q(first_name__icontains=search) |
            Q(email__icontains=search) |
            Q(contact__icontains=search), 
            user_type = 'customer'
        )
        if len(users) == 0:
            messages.error(request, "Utilisateur non trouvé")
    page = request.GET.get('page', 1)
    paginator = Paginator(users, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'tontine_app/accounts.html', {"users": users})