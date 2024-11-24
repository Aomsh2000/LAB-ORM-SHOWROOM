# Generated by Django 5.1.2 on 2024-11-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
