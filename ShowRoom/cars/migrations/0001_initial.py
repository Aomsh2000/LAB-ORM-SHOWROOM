# Generated by Django 5.1.2 on 2024-11-21 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164)),
                ('hex_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164)),
                ('model', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('seats', models.PositiveIntegerField()),
                ('doors', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specs', models.TextField()),
                ('fuel', models.CharField(choices=[('PET', 'Petrol'), ('DIE', 'Diesel'), ('ELE', 'Electric'), ('HYB', 'Hybrid'), ('GAS', 'Gas'), ('LPG', 'LPG'), ('CNG', 'CNG')], default='PET', max_length=64)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
                ('colors', models.ManyToManyField(blank=True, to='cars.color')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
