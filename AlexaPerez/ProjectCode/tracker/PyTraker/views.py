from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, ProfileForm


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
            # newdiary.userID = User.objects.get(userID=request.user)
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
