# Generated by Django 3.2.9 on 2022-01-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_disc_sell_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
    ]