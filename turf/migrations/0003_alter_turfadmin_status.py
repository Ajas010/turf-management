# Generated by Django 5.1.3 on 2024-12-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turfadmin',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=100),
        ),
    ]