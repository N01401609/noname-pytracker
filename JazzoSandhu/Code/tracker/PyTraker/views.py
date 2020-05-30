
from django.http import HttpResponse
# load the template shortcuts
from django.shortcuts import render
from .models import Comments
#if dont have data to display import 404 error
from django.http import Http404
# Create your views here.
def index(request):
    all_comments = Comments.objects.all()
    # create a dictionary to store the values so that we can pass the values from views to the template #
    context = {
        'all_comments': all_comments,
    }
    # pass the values to the template by render threw it
    return render(request, 'PyTraker/comments.html', context)

def detail(request, comments_id):
    try:
        comment = Comments.objects.get(pk=comments_id)
    except Comments.DoesNotExist:
        raise Http404("This file is not Exits")
    return render(request, 'PyTraker/detail.html', {'comment':comment})


