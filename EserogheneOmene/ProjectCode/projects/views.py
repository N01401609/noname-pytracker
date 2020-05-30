from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

# Create your views here.
def index(request):
    latest_project_list = Project.objects.order_by('-start_date')[:10]
   # template = loader.get_template('projects/index.html')
    context = {
        'latest_project_list': latest_project_list,
    }

   # output = ', '.join([p.name for p in latest_project_list])
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'projects/detail.html',{'project': project})
