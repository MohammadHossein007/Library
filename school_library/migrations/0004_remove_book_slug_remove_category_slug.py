# Generated by Django 5.1.4 on 2025-01-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school-library', '0003_alter_author_slug_alter_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
