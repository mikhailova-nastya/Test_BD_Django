# Generated by Django 3.2.9 on 2022-01-04 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_buyer_name_customer_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
    ]
