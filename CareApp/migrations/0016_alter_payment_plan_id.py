# Generated by Django 5.0.2 on 2024-03-29 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0012_alter_driverdb_vehicle_num'),
        ('CareApp', '0015_payment_plan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Plan_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminSide.plans'),
        ),
    ]
