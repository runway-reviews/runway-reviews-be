# Generated by Django 5.0.2 on 2024-02-08 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_remove_reviews_user_alter_reviews_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]