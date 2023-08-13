from django.db import models
import uuid
# Create your models here.

class tag(models.Model):
    tag_name = models.CharField(max_length=20)
    def __str__(self):
        return self.tag_name

class grade(models.Model):
    grade_name = models.CharField(max_length=20)
    def __str__(self):
        return self.grade_name

class teacher(models.Model):
    username = models.CharField(max_length=200)
    teacher_id = models.CharField(max_length=200)
    weba_id  = models.UUIDField(primary_key=True,default =uuid.uuid4)
    def __str__(self):
        return self.username

class student(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to="student_profile/")
    roll_no = models.IntegerField()
    teacher_followers = models.ManyToManyField(teacher)
    grade_in = models.ManyToManyField(grade)
    no_of_messages = models.IntegerField(default=0)
    def __str__(self):
        return self.username
    
class lesson(models.Model):
    author = models.ForeignKey(teacher,on_delete=models.PROTECT)
    lesson_tags = models.ForeignKey(tag,on_delete=models.PROTECT)
    lesson_thumbnail = models.ImageField(upload_to="lesson_thumb/") 
    lesson_name = models.CharField(max_length=200)
    lesson_url = models.URLField(max_length=300, blank=True)
    lesson_date = models.DateTimeField(auto_now_add=True) 
    grade_for = models.ManyToManyField(grade)
    def __str__(self):
        return (f'{self.lesson_name}')
  
class note(models.Model):
    author = models.ForeignKey(teacher,on_delete=models.PROTECT)
    grade_for = models.ManyToManyField(grade)
    chapter_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to="notes_pdf/")
    def __str__(self):
        return self.chapter_name

class notices_by_teacher(models.Model):
    post_by = models.ForeignKey(teacher, on_delete=models.PROTECT)
    notice_title  = models.CharField(max_length=300)
    notice_text = models.TextField(max_length=5000)
    send_to_student = models.ManyToManyField(grade)
    def __str__(self):
        return self.post_by.username

