# Generated by Django 2.0.5 on 2018-07-17 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180717_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follower_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='following_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='no_profile_pic.png', upload_to='avatars'),
        ),
    ]
