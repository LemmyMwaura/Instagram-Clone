# Generated by Django 4.0.3 on 2022-04-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_likes_like_alter_post_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.comment'),
        ),
    ]
