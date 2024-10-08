from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

@admin_or_manager_required
def users(request):
    User = get_user_model()
    users = User.objects.filter(user_type = 'customer').order_by("-date_joined")
    page = request.GET.get('page', 1)
    paginator = Paginator(users, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    if request.method == "POST":
        ID = request.POST.get('id')
        try:
            user = User.objects.get(pk=ID)
            user.delete()
            messages.success(request, "Utilisateur supprimé avec succès.")
        except User.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")
    return render(request, 'tontine_app/users.html', {"users": users} )