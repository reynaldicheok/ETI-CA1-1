from django.shortcuts import render

# Create your views here.
from resume.models import Resume

def project_index(request):
    resume = Resume.objects.all()
    context = {
        'resume': resume
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    resumes = Resume.objects.get(pk=pk)
    context = {
        'resumes': resumes
    }
    return render(request, 'project_detail.html', context)
