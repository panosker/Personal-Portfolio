# Generated by Django 4.2.4 on 2023-09-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contactsubmission_delete_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribproject',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='myproject',
            name='detail',
        ),
    ]
