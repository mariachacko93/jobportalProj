# Generated by Django 3.1.3 on 2020-12-15 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20201215_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addjob',
            name='date_posted',
        ),
    ]