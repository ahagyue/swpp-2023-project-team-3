# Generated by Django 4.2.6 on 2023-10-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0004_alter_item_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
