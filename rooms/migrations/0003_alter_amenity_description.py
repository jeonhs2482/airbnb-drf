# Generated by Django 4.1 on 2022-09-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_amenity_created_at_amenity_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="amenity",
            name="description",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]