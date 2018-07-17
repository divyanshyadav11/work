# Generated by Django 2.0 on 2018-07-03 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_invoice_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Invoice')),
            ],
        ),
    ]
