# Generated by Django 5.0.2 on 2024-03-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0011_alter_driverdb_vehicle_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverdb',
            name='Vehicle_Num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
