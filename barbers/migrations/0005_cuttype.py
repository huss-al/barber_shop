# Generated by Django 4.2.13 on 2024-07-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0004_barber_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]