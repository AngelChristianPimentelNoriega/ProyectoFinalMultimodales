# Generated by Django 4.1.4 on 2022-12-08 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='author',
            new_name='user',
        ),
    ]
