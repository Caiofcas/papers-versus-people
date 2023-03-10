# Generated by Django 4.1.7 on 2023-03-01 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardset",
            name="official",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="text",
            field=models.TextField(unique=True),
        ),
    ]
