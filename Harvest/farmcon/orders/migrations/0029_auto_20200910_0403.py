# Generated by Django 3.0.10 on 2020-09-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20200910_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1599707004.2454758', max_length=120, unique=True),
        ),
    ]
