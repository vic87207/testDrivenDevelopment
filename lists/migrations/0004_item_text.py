# Generated by Django 5.1.5 on 2025-02-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0003_remove_item_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="text",
            field=models.TextField(default=""),
        ),
    ]
