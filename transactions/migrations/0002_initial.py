# Generated by Django 5.2.3 on 2025-06-17 23:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biens', '0002_initial'),
        ('transactions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='bien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biens.bienimmobilier'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_client', to=settings.AUTH_USER_MODEL),
        ),
    ]
