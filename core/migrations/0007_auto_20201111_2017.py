# Generated by Django 3.1.3 on 2020-11-11 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_habit_metric'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='entry_date',
            new_name='date',
        ),
    ]