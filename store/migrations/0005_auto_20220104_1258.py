# Generated by Django 3.2.9 on 2022-01-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_customer_name_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='disc_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='disc_value',
            new_name='value',
        ),
    ]