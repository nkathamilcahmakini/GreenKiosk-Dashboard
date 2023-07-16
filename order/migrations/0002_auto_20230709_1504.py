# Generated by Django 3.2.12 on 2023-07-09 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_delivery_address'),
        ('customer', '0001_initial'),
        ('cart', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery'),
        ),
    ]
