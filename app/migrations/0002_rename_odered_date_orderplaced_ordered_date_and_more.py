# Generated by Django 4.0.4 on 2022-06-08 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='odered_date',
            new_name='ordered_date',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='quantitiy',
            new_name='quantity',
        ),
    ]
