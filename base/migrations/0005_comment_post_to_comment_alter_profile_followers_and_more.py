# Generated by Django 4.0.3 on 2022-04-04 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_profile_followers_alter_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_to_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='my_followers', to='base.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='i_am_following', to='base.profile'),
        ),
    ]
