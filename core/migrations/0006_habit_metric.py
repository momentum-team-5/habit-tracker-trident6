# Generated by Django 3.1.3 on 2020-11-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201109_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='metric',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
