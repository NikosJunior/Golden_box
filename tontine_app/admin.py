from django.contrib import admin
from tontine_app.models import CustomUser, Account, Transaction

class CustomUserAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)