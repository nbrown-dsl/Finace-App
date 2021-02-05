from django.shortcuts import render, get_object_or_404
from .models import Project, Expanse
from django.views.generic import CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .forms import ExpanseForm


def project_list(request):
	return render(request,'budget/project_list.html')#returns budget webpage


def project_detail(request, project_slug):
	project = get_object_or_404(Project, slug=project_slug)
	if request.method == 'POST':
		form = ExpanseForm(request.POST or None) 
		if form.is_valid():
			form.save()
		# if form.is_valid():
		# 	title = form.cleaned_data['title']
		# 	amount = form.cleaned_data['amount']

			# Expanse.objects.create(
			# 	project = project,
			# 	title = title,
			# 	amount = amount).save()
		# return HttpResponseRedirect(project_slug)
		else:
			print(form.errors)
	return render(request,'budget/project_detail.html',{'project':project, 'expanse_list': Expanse.objects.all})	


class ViewBudgets(CreateView):
	model = Project
	template_name = 'budget/add.html'
	fields = ('name', 'budget')# this fields are used to add the name of the budget and the budget itsefl
	"""this is to submit the form"""
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return slugify(self.request.POST['name'])

