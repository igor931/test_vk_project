from django.db import models
from django.urls import reverse
from django.utils import timezone

class Group(models.Model):
	slug = models.SlugField(unique=True)

	def get_absolute_url(self):
		url = reverse('group_posts', args=[self.slug])
		return url

	def __str__(self):
		return self.slug

class Post(models.Model):
	num = models.PositiveIntegerField(null=True, unique=True)
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
		ordering = ('-created',)


class Report(models.Model):
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	group = models.ForeignKey(Group, blank=True, null=True, related_name='report_group')
	slug = models.SlugField(null=True)

	def __str__(self):
		return 'Отчет по группе {}, {}'.format(self.group, self.created)

	def get_absolute_url(self):
		url = reverse('report_posts', args=[self.slug,
											self.created.strftime('%m'),
											self.created.strftime('%d')])
		return url