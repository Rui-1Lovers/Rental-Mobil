# Generated by Django 5.2.3 on 2025-07-12 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_rental_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='user',
        ),
        migrations.AddField(
            model_name='rental',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rental_dikelola', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
