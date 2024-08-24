# Generated by Django 4.1 on 2024-08-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0003_movie_genres"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
    ]