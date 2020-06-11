from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, ProfileForm, CommentRawProduction, CommentForm, ProjectForm, InvoiceForm, WorkDiaryForm
from .models import Invoices, Projects, Clients, Tasks, Timers, Comments, WorkDiary

from .forms import UserForm, ProfileForm, CommentRawProduction, CommentForm, ProjectForm
from .models import Invoices, Projects, Clients, Tasks, Timers, Comments, Profile

# for import date and time
from _datetime import datetime
from django.utils import timezone
from django.template import defaultfilters
from django.utils.dateparse import parse_date


# @login_required
def home(request):
    project_list = Projects.objects.all()
    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context = {'project_list': project_list}

    return render(request, 'PyTraker/index.html', {'page_obj': page_obj})


# return render(request, 'PyTraker/index.html')


def sign_up(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            userN = user_form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + userN)
            return redirect('/PyTraker/login/?next=/')
    else:
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
    return render(request, 'PyTraker/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is None:
                login(request, user)
                messages.info(request, 'Username OR password is incorrect')
                return redirect('login')

        context = {}

    return render(request, 'PyTraker/login.html', context)


def log_out(request):
    if request.method == "POST":
        logout(request)

    messages.info(request, "Logged out successfully!")
    return redirect('/PyTraker/index')


# Invoice Views
def invoice(request, invoices_id):
    obj = Invoices.objects.get(id=invoices_id)
    tasks = Tasks.objects.filter(projectID_id=obj.projectID)
    context = {
        'invoice_id': obj.id,
        'project_id': obj.projectID,
        'project_name':obj.projectID.name,
        'client_name': obj.projectID.clientID.name,
        'client_email': obj.projectID.clientID.email,
        'client_phone': obj.projectID.clientID.phone,
        #'user_fname': obj.userID.firstname,
        #'user_lname': obj.userID.lastname,
        'user_email': obj.userID.email,
        #'user_phone': obj.userID.phonenumber,
        'date_created': obj.dateCreated,
        'date_due': obj.dueDate,
        'hourly_rate': obj.projectID.payRate,
        'tasks_list': tasks,
    }
    return render(request, "PyTraker/invoice.html", context)

def invoice_list (request):
    all_invoices = Invoices.objects.order_by("-dateCreated")
    context = {"all_invoices": all_invoices}
    return render(request, "PyTraker/list_invoice.html", context)

def new_invoice(request):
        invoice_form = InvoiceForm(request.POST or None)
        #Checking if the form is valid
        if invoice_form.is_valid():
            invoice_form.save()
            invoice_form = InvoiceForm()
        context = {
            'invoice_form': invoice_form
        }
        return render(request, "PyTraker/new_invoice.html", context)

def edit_invoice(request, invoices_id):
    invoice =  Invoices.objects.get(pk=invoices_id)
    form = InvoiceForm(instance=invoice)
    if request.method == "POST":
        populated_form = InvoiceForm(request.POST, instance=invoice)
        if populated_form.is_valid():
            populated_form.save()
            form = populated_form
            note = "Invoice has been updated."
            return render(request, 'PyTraker/edit_invoice.html', {'note': note,'invoice_form': form, 'invoice': invoice})

    return render(request, 'PyTraker/edit_invoice.html', {'invoice_form': form, 'invoice': invoice})

#comment page
def comment_view(request):
    obj = Comments.objects.all()
    context ={
        'object': obj
    }
    return render(request, "PyTraker/comment_form.html",context)


def comment_detail_view(request, comment_id):
    obj = Comments.objects.get(id=comment_id)
    context = {
        'comment': obj
    }
    return render(request, "PyTraker/comment_detail.html", context)


def comment_create_view(request):
    if request.method == "POST":
        new_comment = CommentForm()
        current_user = request.user
        my_p = User.objects.get(id=current_user.id)
        new_comment.user = my_p
        new_comment.comment = request.POST.get('comment')
        #new_comment.comment_date = parse_date(request.POST.get('comment_date'))
        new_comment.comment_date = datetime.now()
        print(new_comment.user)
        print(new_comment.comment_date)
        print(new_comment.comment)
        Comments.objects.create(user=new_comment.user,comment=new_comment.comment,comment_date=new_comment.comment_date)
    comments = Comments.objects.all()
    date = datetime.now()
    context = {
        'object': comments,
        'time' : defaultfilters.date(date, "Y-m-d h:i A")
    }
    return render(request, "PyTraker/comment_form.html", context)

def comment_delete(request, comment_id):
    obj = get_object_or_404(Comments, id=comment_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }
    return render(request, "PyTraker/comment_delete.html", context)


#Task Views
def tasklist(request):
    all_task_list = Tasks.objects.order_by("name")
    context = {"all_task_list": all_task_list}
    return render(request, "PyTraker/tasklist.html", context)


def task_detail(request, tasks_id):
    tasks = get_object_or_404(Tasks, pk=tasks_id)
    return render(request, 'PyTraker/task_detail.html', {'tasks': tasks})


#Project Views
def projects(request):
    all_projects = Projects.objects.order_by("name")
    context = {"all_projects": all_projects}
    return render(request, "PyTraker/projects.html", context)


def project_detail(request, projects_id):
    project = get_object_or_404(Projects, pk=projects_id)
    return render(request, 'PyTraker/project_detail.html', project)


def new_project(request):
    if request.method == 'POST':
        filled_form = ProjectForm(request.POST or None)
        if filled_form.is_valid():
            created_project = filled_form.save()
            created_project_pk = created_project.id
            note = 'Your Project with %s has been added.' %(filled_form.cleaned_data['name'])
            filled_form = ProjectForm()
        else:
            created_project_pk = None
            note = "Your project was not created, please try again."
        return render(request, 'PyTraker/new_project.html',
                      {'created_project_pk': created_project_pk, 'new_project': filled_form, 'note': note})
    else:
        form = ProjectForm()
        return render(request, 'PyTraker/new_project.html', {'new_project': form})


def edit_project(request, pk):
    project = Projects.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        filled_form = ProjectForm(request.POST, instance=project)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Project has been updated."
            return render(request, 'PyTraker/edit_project.html', {'note': note,'new_project': form, 'project': project})

    return render(request, 'PyTraker/edit_project.html', {'new_project': form, 'project': project})


def details_project(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    return render(request, 'PyTraker/details_project.html', {'project': project})

def list_projects(request):
    project_list = Projects.objects.order_by('dueDate')
    context = {'project_list': project_list}
    return render(request, 'PyTraker/list_projects.html', context)


def delete_project(request, pk):
    pk = int(pk)
    try:
        project_sel = Projects.objects.get(id=pk)
    except Projects.DoesNotExist:
        return redirect('/PyTraker/index')
    project_sel.delete()
    return redirect('/PyTraker/index')


# Work Diary Views

def workdiary(request):
    all_workdiary = WorkDiary.objects.order_by("name")
    context = {"all_workdiary": all_workdiary}
    return render(request, "PyTraker/workdiary.html", context)


def workdiary_add(request):
    if request.method == "POST":
        # initial_data = {
        # 'userID': request.user.is_authenticated
        # }
        diary_form = WorkDiaryForm(request.POST)
        if diary_form.is_valid():
            newdiary = diary_form.save(commit=False)
            #newdiary.userID = User.objects.get(userID=request.user)
            newdiary.save()
            diaryname = diary_form.cleaned_data.get('name')
            messages.success(request, 'Work Diary:' + diaryname + ' was created successfully!')
            return redirect('/PyTraker/workdiary')
    else:
        diary_form = WorkDiaryForm()
    return render(request, 'PyTraker/workdiary_add.html', {'workdiary_add': diary_form})


def workdiary_edit(request, pk):
    workdiary = get_object_or_404(WorkDiary, pk=pk)
    edit_diary = WorkDiaryForm(instance=workdiary)
    if request.method == "POST":
        diary_form = WorkDiaryForm(request.POST, instance=workdiary)
        if diary_form.is_valid():
            diary_form.save()
            edit_diary = diary_form

            return render(request, 'PyTraker/workdiary_edit.html',
                          {'workdiary_edit': edit_diary, 'workdiary': workdiary})

    return render(request, 'PyTraker/workdiary_edit.html', {'workdiary_edit': edit_diary, 'workdiary': workdiary})


def workdiary_details(request, pk):
    workdiary = get_object_or_404(WorkDiary, pk=pk)
    return render(request, 'PyTraker/workdiary_detail.html', {'workdiary': workdiary})


def workdiary_delete(request, pk):
    workdiary = get_object_or_404(WorkDiary, pk=pk)
    return render(request, 'PyTraker/workdiary_delete.html', {'workdiary': workdiary})


def workdiary_conf_delete(request, pk):
    pk = int(pk)
    del_workdiary = WorkDiary.objects.get(id=pk)
    del_workdiary.delete()

    return redirect('/PyTraker/workdiary')

