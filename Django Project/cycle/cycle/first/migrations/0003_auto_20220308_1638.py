# Generated by Django 3.2.9 on 2022-03-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Hii, write your bio here', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='profile_img/default.jpg', upload_to='profile_img/'),
        ),
    ]
