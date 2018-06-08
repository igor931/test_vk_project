from django.shortcuts import render, get_object_or_404, redirect
from .utils import create_posts
from post.models import Post, Group, Report
from post.tasks import test
from django.views.generic import FormView
from post.forms import *

class Index(FormView):
	def post(self, request):
		template_name = 'index.html'
		slug = request.POST.get('slug')
		result = test.delay(slug)
		result.wait()
		group = Group.objects.get(slug=slug)	
		return redirect(group.get_absolute_url())
	
	def get(self, request):
		template_name = 'index.html'
		groups = Group.objects.all()
		reports = Report.objects.all()
		form = GroupForm()
		context = {'form': form, 'groups': groups, 'reports': reports}
		return render(request, 'index.html', context)

def get_obj(request):
	slug = 'tvoy171090'
	test.delay(slug)
	posts = Post.objects.all()
	return render(request, 'post.html', {'posts': posts})

def group_posts(request, slug):
	group = get_object_or_404(Group, slug=slug)
	posts = Post.objects.filter(group=group).order_by('created',)
	return render(request, 'group_posts.html', {'posts': posts,
												'group': group})
def report_posts(request, slug, month, day):
	report = get_object_or_404(Report, slug=slug, created__month=month, created__day=day)
	return render(request, 'report.html', {'report': report})

def login(request):
	return render(request, 'login.html')
