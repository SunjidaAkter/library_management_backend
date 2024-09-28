# Generated by Django 5.0.4 on 2024-09-28 12:47

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nationality', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=500)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('image', models.URLField(max_length=500)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
