# Generated by Django 5.0.6 on 2024-06-01 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='gastos',
        ),
    ]
