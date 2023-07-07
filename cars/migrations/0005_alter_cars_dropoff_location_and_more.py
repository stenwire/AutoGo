# Generated by Django 4.2.3 on 2023-07-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_alter_cars_booked_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars",
            name="dropoff_location",
            field=models.CharField(max_length=255, verbose_name="Dropoff Location"),
        ),
        migrations.AlterField(
            model_name="cars",
            name="pickup_location",
            field=models.CharField(max_length=255, verbose_name="Pickup Location"),
        ),
    ]