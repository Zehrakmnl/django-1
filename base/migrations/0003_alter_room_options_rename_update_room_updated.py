# Generated by Django 4.2.8 on 2023-12-20 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='update',
            new_name='updated',
        ),
    ]
