# Generated by Django 4.0.4 on 2022-05-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_orderproduct_delete_cartproduct_alter_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_placed',
            field=models.BooleanField(default=False),
        ),
    ]
