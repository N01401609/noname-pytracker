from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to PyTraker")


# CREATE INVOICE VIEW
def invoice(request, invoice_id):
    response = "Invoice for Project %s."
    return HttpResponse(response % invoice_id)
