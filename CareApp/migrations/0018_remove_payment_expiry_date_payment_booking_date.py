# Generated by Django 5.0.3 on 2025-03-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareApp', '0017_chat_alter_registrationdb_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Expiry_Date',
        ),
        migrations.AddField(
            model_name='payment',
            name='Booking_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
