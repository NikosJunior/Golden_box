from django.shortcuts import render,redirect
import secrets
import string
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Account

def is_admin_or_manager(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.user_type == 'manager' or  user.is_staff)

admin_or_manager_required = user_passes_test(is_admin_or_manager)

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
    
@admin_or_manager_required
def signup(request):
    User = get_user_model()
    if (request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        sexe = request.POST.get('sexe')
        address = request.POST.get('address')
        user_type = request.POST.get('user_type')
        password = generate_password()
        payment = request.POST.get('payment')
        if not contact:
            messages.error(request, "Contact requis")
            return redirect("/register")
      
        if not first_name:
            messages.error(request, "Prénom requis")
            return redirect("/register")
        
        if not last_name:
            messages.error(request, "Nom requis")
            return redirect("/register")

        if not address:
            messages.error(request, "Adresse requise")
            return redirect("/register")

        if User.objects.filter(contact=contact).exists():
            messages.info(request, "Contact existant")
            return redirect("/register")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email déjà utilisé")
            return redirect("/register")

        if user_type == 'customer':
            if not payment:
                messages.error(request, "modalité requis pour les clients")
                return redirect("/register")

  
        try:
            user = User.objects.create_user(
                username=email, 
                first_name=first_name,
                last_name=last_name,
                contact=contact,
                email=email,
                sexe=sexe,
                address=address,
                password=password,
                user_type=user_type,  
            )
            messages.success(request, 'Enregistrement fait avec succès')
        except Exception as e:
            messages.error(request, f"Erreur lors de l'enregistrement : {e}")
            return redirect('/register')

        #Création du premier compte utilisateur
        if user.user_type == 'customer':
            try:
                account = Account.objects.create(
                    user = user,
                    payment = payment,
                )
            except Exception as e:
                messages.error(request, f"Erreur lors de la création de compte : {e}" )
                return redirect('/register')




    return render(request, "tontine_app/register.html")


