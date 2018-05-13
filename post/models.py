from django.db import models
from django.core.urlresolvers import reverse

class Group(models.Model):
	slug = models.SlugField(unique=True)

	def get_absolute_url(self):
		url = reverse('group_posts', args=[self.slug])
		return url

	def __str__(self):
		return self.slug

class Post(models.Model):
	text = models.TextField(unique=True)
	url = models.URLField()
	comments = models.PositiveIntegerField()
	likes = models.PositiveIntegerField()
	reposts = models.PositiveIntegerField()
	views = models.PositiveIntegerField()
	group = models.ForeignKey(Group, blank=True, null=True, related_name='group')

	def __str__(self):
		return self.text