# Generated by Django 5.1.5 on 2025-03-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_member_membership_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
