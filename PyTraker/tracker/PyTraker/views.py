from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, ProfileForm
from.models import Invoices,Projects, Clients


@login_required
def index(request):
    return render(request, 'PyTraker/index.html')


def sign_up(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            login(request, user)
            return render(request, 'PyTraker/index.html')
    else:
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
    return render(request, 'PyTraker/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})


def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, 'PyTraker/login.html')


#Invoice View
def invoice_details(request):
    obj = Invoices.objects.get(id=1)
    context = {
        'invoice_id': obj.id,
        'client_name': obj.projectID.clientID.name,
        'client_email': obj.projectID.clientID.email,
        'client_phone': obj.projectID.clientID.phone,
        'user_fname': obj.userID.firstname,
        'user_lname': obj.userID.lastname,
        'user_email': obj.userID.email,
        'user_phone': obj.userID.phonenumber,
        'date_created': obj.dateCreated,
        'due_date': obj.dueDate

    }
    return render(request, "PyTraker/invoice.html", context)

def invoice(request):
    return HttpResponse("Testing...")

