# Generated by Django 3.2.6 on 2021-08-05 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210806_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='date',
        ),
    ]
