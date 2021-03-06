# Generated by Django 2.1.5 on 2020-07-17 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picked_up', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('andrew_id', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('profile_pic', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(default='image/jpg', max_length=50)),
                ('customer', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20)),
                ('customer_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='takeout.CustomerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_detail', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('number_ordered', models.IntegerField(default=0)),
                ('avail_quantity', models.IntegerField()),
                ('drink', models.CharField(max_length=50)),
                ('meal_type', models.CharField(max_length=20)),
                ('meal_name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(default='image/jpg', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('company_name', models.CharField(max_length=20)),
                ('license', models.CharField(max_length=100)),
                ('time_slot', models.CharField(max_length=200)),
                ('parking_location', models.CharField(max_length=200)),
                ('car', models.CharField(max_length=200)),
                ('profile_pic', models.FileField(blank=True, upload_to='')),
                ('content_type', models.CharField(default='image/jpg', max_length=50)),
                ('payment_key', models.CharField(max_length=50)),
                ('vendor', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='vendor_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='vendormeal',
            name='vendor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='takeout.VendorProfile'),
        ),
        migrations.AddField(
            model_name='customermeal',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='takeout.Order'),
        ),
        migrations.AddField(
            model_name='customermeal',
            name='vendor_meal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='takeout.VendorMeal'),
        ),
    ]
