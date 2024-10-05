# Generated by Django 5.1 on 2024-09-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine_app', '0002_account_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='transaction_date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'Espece'), ('online', 'En ligne')], default='cash', max_length=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('deposit', 'Depot'), ('withdraw', 'retrait')], default='deposit', max_length=10),
        ),
    ]
