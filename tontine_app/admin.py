from django.contrib import admin
from tontine_app.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
