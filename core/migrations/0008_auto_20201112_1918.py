# Generated by Django 3.1.3 on 2020-11-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201111_2017'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='unique_record'),
        ),
    ]
