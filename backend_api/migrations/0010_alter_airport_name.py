# Generated by Django 5.0.2 on 2024-02-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_alter_review_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
