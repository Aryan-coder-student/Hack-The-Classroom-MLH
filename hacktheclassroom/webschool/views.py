from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth.decorators import login_required
from .models import *
import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')
def login_form_student(request):
    return render(request,'login_student.html')
def login_form_teacher(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        mail = request.POST.get('email')
        pas = request.POST.get('password')
        # print(u_name,pas,mail)
        check_detail = User.objects.all()
        
        check_detail = auth.authenticate(username=u_name, email= mail, password=pas)
        if check_detail is not None:
            try:
                t_find = teacher.objects.get(username=check_detail.username)
                auth.login(request,check_detail)
                
                return redirect('/TeacherPortal')
            except:
                t_save = teacher.objects.create(username=check_detail.username, teacher_id=check_detail.email)
                t_save.save()
                auth.login(request,check_detail)
                return redirect('/TeacherPortal')
        else:
            print('Teacher not found ask your administrator')
            return render(request,'login_teacher.html')
    return render(request,'login_teacher.html')
@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/TeacherLogin')
@login_required(login_url='/')
def teacher_page(request):
    details =  lesson.objects.filter(author__username=request.user)
    chapter_list = []
    for i in details :
        if (i.lesson_tags == tag.objects.get(tag_name='Recording')):
            chapter_list.append(i)
    for x in details:
        if (x.lesson_date.date() >= datetime.datetime.now().date() and x.lesson_tags == tag.objects.get(tag_name="Live")):
            chapter_list.append(x)
    context = {'details':  chapter_list ,'rec':tag.objects.filter(tag_name='Recording')}

    return render(request,'teacher_page.html' , context)

@login_required(login_url='/')
def lessons(request):
    no_of_grads = len(grade.objects.all())
    if request.method == 'POST':
        l_name = request.POST.get('l_name')
        l_url = request.POST.get('l_url')
        l_thumbnail = request.FILES.get('l_thumbnail')
        
        l_or_r = "Live"
        if request.POST.get('Live') is None:
            l_or_r = 'Recording'
        lorrtag = tag.objects.get(tag_name=l_or_r)
        
        l_class = request.POST.get('l_class')
        t_l = teacher.objects.get(username=request.user)

        l_save = lesson.objects.create(author=t_l,lesson_tags = lorrtag , lesson_thumbnail = l_thumbnail ,lesson_name = l_name , lesson_url = l_url, lesson_date = l_class)
    
        for i in range(1,no_of_grads):
            c_l = request.POST.get(f'check {i}')
            if c_l is not None:
                grade_tag = grade.objects.get(grade_name=c_l)
                l_save.grade_for.add(grade_tag)   
        l_save.save()
    return render(request,'lesson.html')

@login_required(login_url='/')
def create_notes(request):
    no_of_grads = len(grade.objects.all())
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_title = request.POST.get('c_title')
        c_pdf = request.FILES.get('c_pdf')
        t_n = teacher.objects.get(username=request.user)
        c_n_save = note.objects.create(author=t_n , pdf_file = c_pdf ,chapter_name= c_name , title= c_title)
        for i in range(1,no_of_grads):
            c_l = request.POST.get(f'check {i}')
            if c_l is not None:
                grade_tag = grade.objects.get(grade_name=c_l)
                c_n_save.grade_for.add(grade_tag)   
        c_n_save.save()
    return render(request,'notes.html')

@login_required(login_url='/')
def my_notes(request):
    notes_by_teacher = note.objects.filter(author__username=request.user)
    context = {'notes_by_teacher': notes_by_teacher}
    return render(request,'my_notes.html',context)
@login_required(login_url='/')
def notices(request):
    no_of_grads = len(grade.objects.all())
    t_n = teacher.objects.get(username=request.user)
    if request.method == 'POST':
        n_title = request.POST.get('n_title')
        body = request.POST.get('notice_send')
        n_b_t = notices_by_teacher.objects.create(post_by= t_n ,notice_title= n_title, notice_text = body)
        for i in range(1,no_of_grads):
            c_l = request.POST.get(f'check {i}')
            if c_l is not None:
                grade_tag = grade.objects.get(grade_name=c_l)
                n_b_t.send_to_student.add(grade_tag)   
        n_b_t.save()
    return render(request,'send_notice.html')
@login_required(login_url='/')
def past_class (request):
    chapter = lesson.objects.filter(author__username = request.user)
    chapter_list = []
    for x in chapter:
        if (x.lesson_date.date() < datetime.datetime.now().date() and x.lesson_tags == tag.objects.get(tag_name="Live")):
            chapter_list.append(x)
    context = {'chapter_list': chapter_list}
    return render(request,'past_class.html',context)
@login_required(login_url='/')
def past_notices(request):
    n_h = notices_by_teacher.objects.filter(post_by__username=request.user)
    context = {'n_h': n_h}
    return render(request,'past_notice.html',context)