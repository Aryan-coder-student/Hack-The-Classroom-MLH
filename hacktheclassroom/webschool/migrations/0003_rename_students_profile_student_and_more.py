# Generated by Django 4.2.3 on 2023-08-05 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0002_tag_lesson'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students_profile',
            new_name='student',
        ),
        migrations.RenameModel(
            old_name='teacher_info',
            new_name='teacher',
        ),
    ]
