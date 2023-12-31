# Generated by Django 4.2.3 on 2023-08-09 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0010_remove_lesson_l_or_r_tag_lesson_l_or_r_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='l_or_r_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webschool.tag'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_thumbnail',
            field=models.ImageField(upload_to='lesson_thumb/'),
        ),
    ]
