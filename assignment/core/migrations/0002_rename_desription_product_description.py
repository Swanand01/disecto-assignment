# Generated by Django 4.0.4 on 2022-05-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desription',
            new_name='description',
        ),
    ]
