# Generated by Django 4.2.3 on 2023-08-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0012_remove_lesson_l_or_r_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_thumbnail',
            field=models.ImageField(default='SOME STRING', upload_to='lesson_thumb/'),
        ),
    ]
