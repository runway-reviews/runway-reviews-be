# Generated by Django 5.0.2 on 2024-02-09 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0005_merge_0003_rename_reviews_review_0004_airport_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_api.airport'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_api.user'),
        ),
    ]