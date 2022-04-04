# Generated by Django 4.0.3 on 2022-04-04 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='base.like'),
        ),
    ]
