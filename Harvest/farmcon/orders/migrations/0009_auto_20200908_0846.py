# Generated by Django 3.1 on 2020-09-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200908_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1599551188.9265318', max_length=120, unique=True),
        ),
    ]
