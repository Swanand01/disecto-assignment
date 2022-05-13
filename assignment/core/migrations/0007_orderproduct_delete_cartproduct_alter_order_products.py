# Generated by Django 4.0.4 on 2022-05-13 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_order_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='core.orderproduct'),
        ),
    ]