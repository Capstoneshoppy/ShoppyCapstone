# Generated by Django 2.2.14 on 2021-10-22 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_orderitemmodel_orderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemmodel',
            name='order',
        ),
    ]