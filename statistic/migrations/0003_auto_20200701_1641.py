# Generated by Django 3.0.7 on 2020-07-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_auto_20200701_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='data',
            new_name='date',
        ),
    ]
