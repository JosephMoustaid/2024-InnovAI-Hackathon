# Generated by Django 5.1.2 on 2024-10-25 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_archive_total_sales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='drug',
        ),
    ]