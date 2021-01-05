from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
	return render(request,'budget/project-list.html')#returns budget webpage

def project_detail(request, project_slug):
	project = get_object_or_404(Project, slug=project_slug)
	expanse_list = project.expanses
	return render(request,'budget/project-detail.html',{'project':project, 'expanse_list': project.expanses.all()})#handels project requests
