# Generated by Django 5.1 on 2024-09-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tontine_app', '0003_rename_date_transaction_transaction_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='solde',
            new_name='balance',
        ),
    ]
