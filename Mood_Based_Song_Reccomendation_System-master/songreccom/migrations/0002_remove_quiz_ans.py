# Generated by Django 4.0 on 2023-02-14 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songreccom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='ans',
        ),
    ]
