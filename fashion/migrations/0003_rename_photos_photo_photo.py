# Generated by Django 5.0.1 on 2024-02-03 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0002_sweatshirt_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photos',
            new_name='photo',
        ),
    ]
