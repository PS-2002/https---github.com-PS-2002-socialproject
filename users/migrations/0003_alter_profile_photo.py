# Generated by Django 5.0.3 on 2024-07-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='imageă019_avatar_male_man_person_user_icon.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
