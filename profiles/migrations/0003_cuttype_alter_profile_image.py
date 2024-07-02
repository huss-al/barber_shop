# Generated by Django 4.2.13 on 2024-07-02 13:40

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('duration', models.IntegerField(default=30)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://www.example.com/default-image.jpg', max_length=255),
        ),
    ]