# Generated by Django 4.2.3 on 2023-08-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0007_remove_lesson_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_thumbnail',
            field=models.ImageField(default='SOME STRING', upload_to='lesson_thumb/'),
        ),
    ]
