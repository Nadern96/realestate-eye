# Generated by Django 4.2.9 on 2024-01-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_companyreview_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyreview",
            name="land_num",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
