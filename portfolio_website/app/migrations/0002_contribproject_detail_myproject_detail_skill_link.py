# Generated by Django 4.2.4 on 2023-08-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribproject',
            name='detail',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='myproject',
            name='detail',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]