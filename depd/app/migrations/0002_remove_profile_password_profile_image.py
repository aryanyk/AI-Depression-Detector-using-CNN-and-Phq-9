# Generated by Django 5.1.2 on 2024-10-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="password",
        ),
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]