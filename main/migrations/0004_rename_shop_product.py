# Generated by Django 5.1.1 on 2024-10-02 04:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shop_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='Product',
        ),
    ]
