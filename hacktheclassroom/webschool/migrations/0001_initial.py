# Generated by Django 4.2.3 on 2023-08-05 11:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_info',
            fields=[
                ('username', models.CharField(max_length=200)),
                ('teacher_id', models.CharField(max_length=200)),
                ('profile_photo', models.ImageField(upload_to='teacher_profile/')),
                ('weba_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='students_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('profile_photo', models.ImageField(upload_to='student_profile/')),
                ('grade', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('teacher_followers', models.ManyToManyField(to='webschool.teacher_info')),
            ],
        ),
    ]
