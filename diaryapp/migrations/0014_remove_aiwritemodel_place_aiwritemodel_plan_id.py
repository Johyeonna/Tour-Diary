# Generated by Django 4.1.13 on 2024-08-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diaryapp", "0013_alter_aiwritemodel_representative_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aiwritemodel",
            name="place",
        ),
        migrations.AddField(
            model_name="aiwritemodel",
            name="plan_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
