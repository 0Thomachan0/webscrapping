# Generated by Django 4.1 on 2023-10-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Links",
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
                ("address", models.CharField(blank=True, max_length=500, null=True)),
                ("stringname", models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
