# Generated by Django 3.0.6 on 2020-06-24 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_auto_20200624_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='num',
            new_name='num_newspaper',
        ),
    ]
