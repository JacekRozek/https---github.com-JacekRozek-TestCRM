# Generated by Django 4.1.3 on 2023-01-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_alter_contract_client_alter_contract_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]
