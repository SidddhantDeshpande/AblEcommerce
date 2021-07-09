# Generated by Django 3.2.3 on 2021-07-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]