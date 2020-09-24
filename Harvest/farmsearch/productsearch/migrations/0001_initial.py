# Generated by Django 3.1.1 on 2020-09-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('slug', models.SlugField(unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=10)),
                ('in_stock', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('title', 'slug')},
            },
        ),
    ]
