# Generated by Django 4.2.7 on 2023-11-28 01:09

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                default="static/images/default_profile_image.jpg",
                null=True,
                upload_to=apps.user.models.user_image,
            ),
        ),
    ]
