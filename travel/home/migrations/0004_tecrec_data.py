# Generated by Django 4.1.7 on 2023-03-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_contact_zip"),
    ]

    operations = [
        migrations.CreateModel(
            name="tecRec_data",
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
                ("campaign_pic", models.ImageField(upload_to="static/opspage_pics")),
            ],
        ),
    ]
