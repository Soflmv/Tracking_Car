# Generated by Django 4.1.2 on 2022-10-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=20)),
                ('driver', models.CharField(max_length=30)),
                ('car_number', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=15)),
                ('speed', models.CharField(max_length=5)),
                ('coordinates', models.CharField(max_length=30)),
            ],
        ),
    ]