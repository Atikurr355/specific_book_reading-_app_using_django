# Generated by Django 3.2.4 on 2021-08-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_content_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField()),
                ('qualifications', models.TextField()),
                ('links', models.URLField()),
            ],
        ),
    ]