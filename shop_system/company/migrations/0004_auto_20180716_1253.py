# Generated by Django 2.0 on 2018-07-16 12:53

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180702_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/media/logo')),
        ),
    ]
