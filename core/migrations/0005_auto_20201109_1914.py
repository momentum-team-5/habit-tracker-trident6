# Generated by Django 3.1.3 on 2020-11-09 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201109_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='habit',
            new_name='user',
        ),
    ]
