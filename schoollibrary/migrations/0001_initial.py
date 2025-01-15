# Generated by Django 5.1.5 on 2025-01-15 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='نام نویسنده')),
                ('bio', models.TextField(blank=True, verbose_name='بیوگرافی')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسنده ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, default='no-image-available-icon-vector.jpg', upload_to='', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('first_name', models.CharField(max_length=128, verbose_name='نام')),
                ('last_name', models.CharField(max_length=128, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='آدرس ایمیل')),
                ('phone_number', models.CharField(blank=True, max_length=11, unique=True, verbose_name='شماره تلفن')),
                ('membership_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='کد عضویت')),
                ('membership_start_date', models.DateField(auto_now_add=True, verbose_name='تاریخ شروع عضویت')),
                ('membership_end_date', models.DateField(blank=True, null=True, verbose_name='تاریخ پایان عضویت')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'عضو',
                'verbose_name_plural': 'اعضاء',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, default='no-image-available-icon-vector.jpg', upload_to='', verbose_name='تصویر')),
                ('placed_at', models.DateField(auto_now=True, verbose_name='تاریخ اضافه شدن')),
                ('is_available', models.BooleanField(default=True, verbose_name='موجود')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoollibrary.author', verbose_name='نویسنده')),
                ('category', models.ManyToManyField(to='schoollibrary.category', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_on', models.DateField(auto_now_add=True, verbose_name='تاریخ بردن')),
                ('return_by', models.DateField(verbose_name='تاریخ برگشت')),
                ('status', models.CharField(choices=[('borrowed', 'قرض گرفته شده'), ('returned', 'برگردانده شده'), ('overdue', 'عقب افتاده')], default='borrowed', max_length=32, verbose_name='وضعیت')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schoollibrary.book', verbose_name='کتاب')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schoollibrary.member', verbose_name='عضو')),
            ],
            options={
                'verbose_name': 'امانت',
                'verbose_name_plural': 'امانت ها',
            },
        ),
    ]
