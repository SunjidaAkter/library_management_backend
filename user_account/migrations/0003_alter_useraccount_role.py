# Generated by Django 5.0.4 on 2024-10-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_remove_useraccount_image_useraccount_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('Reader', 'Reader'), ('Admin', 'Admin')], default='Reader', max_length=10),
        ),
    ]
