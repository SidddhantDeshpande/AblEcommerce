# Generated by Django 3.2.3 on 2021-07-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
    ]