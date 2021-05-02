# Generated by Django 2.1.7 on 2020-06-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banglorejob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hyderabadjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Indorejob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Punejob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
