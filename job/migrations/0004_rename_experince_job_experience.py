# Generated by Django 4.2.3 on 2023-07-27 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='experince',
            new_name='experience',
        ),
    ]
