# Generated by Django 4.2.10 on 2024-05-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="property_images/"
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="landlord_contact",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
