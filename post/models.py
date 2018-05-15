from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Group(models.Model):
	slug = models.SlugField(unique=True)

	def get_absolute_url(self):
		url = reverse('group_posts', args=[self.slug])
		return url

	def __str__(self):
		return self.slug

class Post(models.Model):
	num = models.PositiveIntegerField(null=True)
	text = models.TextField()
	url = models.URLField()
	comments = models.PositiveIntegerField()
	likes = models.PositiveIntegerField()
	reposts = models.PositiveIntegerField()
	views = models.PositiveIntegerField(null=True)
	group = models.ForeignKey(Group, blank=True, null=True, related_name='group')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	class Meta:
		ordering = ('created',)