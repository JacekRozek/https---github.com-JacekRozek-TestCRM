# Generated by Django 4.1.3 on 2023-01-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='department',
            field=models.CharField(default='', help_text='Name of department', max_length=50),
        ),
        migrations.AddField(
            model_name='contract',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.CharField(help_text='Lastname and Firstname', max_length=150),
        ),
        migrations.AlterField(
            model_name='contract',
            name='release_date',
            field=models.DateField(default='', help_text='Format YYYY-MM-DD', null=True),
        ),
    ]
