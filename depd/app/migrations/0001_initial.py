# Generated by Django 5.1.2 on 2024-10-18 07:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
            ],
        ),
    ]