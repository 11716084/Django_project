# Generated by Django 3.2.6 on 2021-08-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
