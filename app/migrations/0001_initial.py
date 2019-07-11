# Generated by Django 2.0 on 2019-07-11 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('city_id', models.CharField(max_length=200)),
                ('country_id', models.CharField(max_length=200)),
                ('state_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('review', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('Orderdate', models.DateField(auto_now_add=True)),
                ('ordertime', models.TimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=50)),
                ('status', models.CharField(default='Pending', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_name', models.CharField(max_length=200)),
                ('Service_img', models.FileField(blank=True, default='set.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('country_id', models.CharField(max_length=200)),
                ('state_id', models.CharField(max_length=200)),
                ('city_id', models.CharField(max_length=200)),
                ('service', models.CharField(default='test', max_length=200)),
                ('sub', models.CharField(default='test', max_length=200)),
                ('profile_img', models.FileField(blank=True, default='set.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubService_name', models.CharField(max_length=50)),
                ('Service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Service_detail')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='service_provider',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='Service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Service_detail'),
        ),
        migrations.AddField(
            model_name='order',
            name='Sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sub_service'),
        ),
        migrations.AddField(
            model_name='order',
            name='service_provider_assign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Service_provider'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='allinfo',
            name='Service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Service_detail'),
        ),
        migrations.AddField(
            model_name='allinfo',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sub_service'),
        ),
    ]
