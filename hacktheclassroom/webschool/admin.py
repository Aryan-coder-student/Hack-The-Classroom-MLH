from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(tag)
admin.site.register(lesson)
admin.site.register(grade)
admin.site.register(note)
admin.site.register(notices_by_teacher)