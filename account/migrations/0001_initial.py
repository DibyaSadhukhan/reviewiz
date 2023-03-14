# Generated by Django 4.1.7 on 2023-03-14 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Email')),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=255)),
                ('Middle_Name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Last_Name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('users', models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
