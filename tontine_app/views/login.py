from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signin(request):
    User = get_user_model()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = None

        if name.isdigit():
            contact = name
            try:
                user = User.objects.get(contact=contact)
            except User.DoesNotExist:
                messages.error(request, "Contact invalide.")
                return redirect('/login')
        else:
            username = name
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, "Nom d'utilisateur invalide.")
                return redirect('/login')

        if user:
            if check_password(password, user.password):
                login(request, user)  # Authentifier l'utilisateur et ouvrir une session
                
                if user.user_type == 'customer':
                    return redirect(f'/user_home/{user.pk}')
                elif user.user_type == 'manager':
                    return redirect('/')
                elif user.user_type == 'admin':
                    return redirect('/')
            else:
                messages.error(request, "Mot de passe incorrect.")
                return redirect('/login')
        else:
            messages.error(request, "Aucun utilisateur trouvé.")
            return redirect('/login')

    return render(request, "tontine_app/login.html")
