# Generated by Django 2.2.1 on 2019-05-15 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
