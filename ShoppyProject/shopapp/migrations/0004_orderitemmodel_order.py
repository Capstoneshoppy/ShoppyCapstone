# Generated by Django 2.2.14 on 2021-10-22 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_remove_orderitemmodel_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.OrderModel'),
        ),
    ]
