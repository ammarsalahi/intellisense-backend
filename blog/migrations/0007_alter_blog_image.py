# Generated by Django 4.1 on 2022-08-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs/7687712900671/",
                verbose_name="main image",
            ),
        ),
    ]
