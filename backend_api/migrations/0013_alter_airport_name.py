# Generated by Django 5.0.2 on 2024-02-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_alter_airport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
