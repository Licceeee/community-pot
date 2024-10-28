# Generated by Django 5.1.2 on 2024-10-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learncraft", "0006_videoupload_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="chapter_nr",
            field=models.PositiveIntegerField(
                help_text="Order of the lesson.", verbose_name="Order"
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="section_nr",
            field=models.PositiveIntegerField(
                help_text="Order of the lesson.", verbose_name="Order"
            ),
        ),
    ]