# Generated by Django 4.1.7 on 2023-05-09 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0002_cardset_official_alter_card_text"),
        ("matches", "0004_alter_match_czar_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="current_black_card",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="cards.card",
            ),
        ),
    ]
