# Generated by Django 5.0.2 on 2024-02-10 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_rename_user_id_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(choices=[('Security', 'Security'), ('Restaurants', 'Restaurants'), ('Rathrooms', 'Bathrooms'), ('General', 'General'), ('Amenities', 'Amenities'), ('Accessibility', 'Accessibility')]),
        ),
    ]
