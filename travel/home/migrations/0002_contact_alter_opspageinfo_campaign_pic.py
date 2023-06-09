# Generated by Django 4.1.7 on 2023-03-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("First_name", models.CharField(max_length=20)),
                ("Last_name", models.CharField(max_length=20)),
                ("username", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("zip", models.IntegerField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("desc", models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name="opspageinfo",
            name="campaign_pic",
            field=models.ImageField(upload_to="static/opspage_pics"),
        ),
    ]
