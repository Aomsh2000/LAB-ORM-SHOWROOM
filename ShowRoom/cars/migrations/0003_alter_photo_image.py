# Generated by Django 5.1.2 on 2024-11-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_photo_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
