# Generated by Django 3.0.3 on 2020-02-16 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200217_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestamp',
            new_name='datetime',
        ),
    ]
