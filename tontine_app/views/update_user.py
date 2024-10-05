from django.shortcuts import render,redirect
import secrets
import string
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or  user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
    
@admin_or_manager_required
def update_user(request, pk):
    User = get_user_model()
    user_to_update= User.objects.get(pk=pk)
    User_type = User.user_type
    print(User_type)
    if (request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        sexe = request.POST.get('sexe')
        address = request.POST.get('address')
        user_type = request.POST.get('user_type')
        password = generate_password()
        print(password)
        if not contact:
            messages.error(request, "Contact requis")
            return redirect(f"/update_user/{pk}")
      
        if not first_name:
            messages.error(request, "Prénom requis")
            return redirect(f"/update_user/{pk}")
        
        if not last_name:
            messages.error(request, "Nom requis")
            return redirect(f"/update_user/{pk}")

        if not address:
            messages.error(request, "Adresse requise")
            return redirect(f"/update_user/{pk}")

        if User.objects.filter(contact=contact).exclude(pk=pk).exists():
            messages.error(request, "Ce contact est déjà utilisé par un autre utilisateur.")
            return redirect(f"/update_user/{pk}")

        if User.objects.filter(email=email).exclude(pk=pk).exists():
            messages.error(request, "Cet email est déjà utilisé par un autre utilisateur.")
            return redirect(f"/update_user/{pk}")
     
        user_to_update.username = email
        user_to_update.first_name=first_name
        user_to_update.last_name=last_name
        user_to_update.contact = contact
        user_to_update.email=email
        user_to_update.sexe = sexe
        user_to_update.address = address
        user_to_update.set_password(password)
        user_to_update.save()
        messages.info(request,'Modification fait avec succès')
    return render(request, "tontine_app/update_user.html", { 'user_to_update': user_to_update })


