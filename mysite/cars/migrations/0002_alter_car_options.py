# Generated by Django 4.1.3 on 2023-01-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name_plural': 'cars'},
        ),
    ]
