# Generated by Django 4.2.6 on 2023-10-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search", "0002_chatlog_first_query"),
    ]

    operations = [
        migrations.AddField(
            model_name="userchat",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]