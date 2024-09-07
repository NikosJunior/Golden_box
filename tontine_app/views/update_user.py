from django.shortcuts import render,redirect
import secrets
import string
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager')

admin_or_manager_required = user_passes_test(is_admin_or_manager)

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
    
@admin_or_manager_required
def update_user(request, pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    if (request.method == 'POST'):
        first_name = request.POST.get('first_name')
        print(first_name)
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
   
  
        user.username = last_name
        user.first_name=first_name
        user.last_name=last_name
        user.contact = contact
        user.email=email
        user.sexe = sexe
        user.address = address
        user.set_password(password)
        user.save()
        messages.info(request,'Modification fait avec succès')
    return render(request, "tontine_app/update_user.html", {'user': user})


