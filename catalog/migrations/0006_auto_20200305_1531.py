# Generated by Django 3.0.4 on 2020-03-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200305_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='services',
        ),
        migrations.AddField(
            model_name='clinic',
            name='services',
            field=models.ManyToManyField(null=True, to='catalog.ClinicServices'),
        ),
    ]