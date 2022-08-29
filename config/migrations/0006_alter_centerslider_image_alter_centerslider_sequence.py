# Generated by Django 4.1 on 2022-08-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0005_centerslider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="centerslider",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs/82685285927141/",
                verbose_name="image",
            ),
        ),
        migrations.AlterField(
            model_name="centerslider",
            name="sequence",
            field=models.IntegerField(null=True),
        ),
    ]
