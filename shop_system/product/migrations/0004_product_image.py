# Generated by Django 2.0 on 2018-07-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180723_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='home/ubox79/Downloads/logo.jpg', upload_to='media'),
        ),
    ]
