# Generated by Django 4.1.7 on 2023-02-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialShare', '0002_comment_credential_message_title_message_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
