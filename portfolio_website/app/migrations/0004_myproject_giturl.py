# Generated by Django 4.2.4 on 2023-08-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_contribproject_image_remove_myproject_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='giturl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
