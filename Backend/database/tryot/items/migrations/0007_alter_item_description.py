# Generated by Django 4.2.6 on 2023-10-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0006_alter_brand_id_alter_category_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(),
        ),
    ]