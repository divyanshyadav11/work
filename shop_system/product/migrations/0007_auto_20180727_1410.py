# Generated by Django 2.0 on 2018-07-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
