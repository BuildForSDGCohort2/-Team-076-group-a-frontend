# Generated by Django 3.0.10 on 2020-09-10 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20200910_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='1599707429.0818863', max_length=120, unique=True),
        ),
    ]
