# Generated by Django 3.2.25 on 2024-12-07 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]