# Generated by Django 3.0.7 on 2020-07-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_auto_20200701_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='date',
            new_name='date_js',
        ),
    ]
