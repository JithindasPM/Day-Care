# Generated by Django 5.0.2 on 2024-03-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driverdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
                ('Mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('Username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('Email', models.EmailField(blank=True, max_length=20, null=True, unique=True)),
                ('Address1', models.CharField(blank=True, max_length=90, null=True)),
                ('Address2', models.CharField(blank=True, max_length=90, null=True)),
                ('Pin_Code', models.CharField(blank=True, max_length=10, null=True)),
                ('License_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('ID_Image', models.ImageField(upload_to='Driver Documents')),
                ('Message', models.CharField(blank=True, max_length=10, null=True)),
                ('Verified', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
