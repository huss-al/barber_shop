# Generated by Django 4.2.13 on 2024-07-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(default='https://www.example.com/default-image.jpg', max_length=255),
        ),
    ]
