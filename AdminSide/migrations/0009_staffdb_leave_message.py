# Generated by Django 5.0.2 on 2024-03-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0008_staffdb_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdb',
            name='Leave_Message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
