from django.shortcuts import render, get_object_or_404, redirect
from .utils import create_posts
from post.models import Post, Group
from post.tasks import test
from django.views.generic import FormView
from post.forms import *

class Index(FormView):
	def post(self, request):
		template_name = 'index.html'
		print('delay')
		slug = request.POST.get('slug')
		print(slug)
		test.delay(slug)
		#group = Group.objects.get(slug=slug)	
		return redirect('/post/')
	
	def get(self, request):
		template_name = 'index.html'
		groups = Group.objects.all()
		form = GroupForm()
		context = {'form': form, 'groups': groups}
		return render(request, 'index.html', context)

def get_obj(request):
	slug = 'tvoy171090'
	test.delay(slug)
	posts = Post.objects.all()
	return render(request, 'post.html', {'posts': posts})

def group_posts(request, slug):
	group = get_object_or_404(Group, slug=slug)
	posts = Post.objects.filter(group=group)
	return render(request, 'group_posts.html', {'posts': posts,
												'group': group})

def login(request):
	return render(request, 'login.html')
