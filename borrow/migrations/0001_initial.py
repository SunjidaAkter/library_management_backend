# Generated by Django 5.0.4 on 2024-09-28 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('user_account', '0002_remove_useraccount_image_useraccount_image_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_after_borrow', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='book.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='borrowers', to='user_account.useraccount')),
            ],
        ),
    ]
