from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import check_password 

def signin(request):
    User = get_user_model()

    if(request.method == 'POST'):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        try:
            user =  User.objects.get(contact = contact)
        except User.DoesNotExist:
            user = None

        if (user == None):
            messages.error(request,'Contact invalide')
            redirect('/login')
             
        else :
            flag = check_password(password, user.password) 
            if flag :
                login(request, user)
     
            if user.user_type == 'customer':
                return redirect(f'/user_home/{user.pk}')

            
            if(user.user_type == 'manager'):
                return redirect('/')

            if(user.user_type == 'admin'):
                return redirect('/')

            
            

   
    return render(request, "tontine_app/login.html")


