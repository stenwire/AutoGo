# Generated by Django 4.2.3 on 2023-07-06 10:06

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_reviews_created_reviews_last_updated_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="booked_by",
            field=models.UUIDField(blank=True, default=uuid.uuid4, unique=True),
        ),
    ]
