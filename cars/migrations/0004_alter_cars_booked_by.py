# Generated by Django 4.2.3 on 2023-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_cars_booked_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars",
            name="booked_by",
            field=models.UUIDField(blank=True),
        ),
    ]