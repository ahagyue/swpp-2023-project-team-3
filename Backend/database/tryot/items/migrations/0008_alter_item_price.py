# Generated by Django 4.2.6 on 2023-10-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0007_alter_item_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
