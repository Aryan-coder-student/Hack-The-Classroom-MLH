# Generated by Django 4.2.3 on 2023-08-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0008_lesson_lesson_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='l_or_r_tag',
            field=models.ManyToManyField(blank=True, to='webschool.tag'),
        ),
    ]
