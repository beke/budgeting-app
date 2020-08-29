# Generated by Django 3.1 on 2020-08-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('business_phone_number', models.CharField(max_length=250)),
                ('business_email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('schema', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]
