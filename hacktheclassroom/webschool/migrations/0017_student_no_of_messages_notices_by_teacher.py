# Generated by Django 4.2.3 on 2023-08-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0016_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='no_of_messages',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='notices_by_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=300)),
                ('notice_text', models.TextField(max_length=5000)),
                ('post_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webschool.teacher')),
                ('send_to_student', models.ManyToManyField(to='webschool.grade')),
            ],
        ),
    ]
