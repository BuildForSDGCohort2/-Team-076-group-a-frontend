# Generated by Django 3.1 on 2020-09-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200908_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1599552254.2393186', max_length=120, unique=True),
        ),
    ]
