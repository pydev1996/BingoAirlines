# Generated by Django 4.2.2 on 2023-06-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bingo', '0007_airline_companies_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline_companies',
            name='logo',
            field=models.ImageField(blank=True, default='/airline_logos/airplanelogo.png', null=True, upload_to='airline_logos/'),
        ),
    ]
