# Generated by Django 4.0.3 on 2022-04-04 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_comment_post_to_comment_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_to_comment',
        ),
    ]
