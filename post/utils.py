import vk
from .models import Post, Group
from django.utils import timezone


login = '+79201673161'
password = 'igorvica2408'
vk_id = '6475437'
access_token = 'd42b18b2228780da05a56213422562392750097bcb6fb77ac4d43e03a5a0695ca349a5ea38a94e9b46a77'

dom = 'https://vk.com/'
domain = 'sociate'

#session = vk.AuthSession(app_id=vk_id, user_login=login, user_password=password)
#def authent():
session = vk.Session(access_token=access_token)
api = vk.API(session, v='5.74')

def get_posts(slug):
	response=api.wall.get(domain=slug, count=100)
	post = response['items']
	print('OK1')
	return post

def create_posts(slug):
	p = get_posts(slug)
	group = Group.objects.get_or_create(slug=slug)[0]
	posts = Post.objects.filter(group=group)
	for i in range(1, 100):
		post = p[i]
		url = dom + slug +'?w=wall' + str(post['from_id']) + '_' + str(post['id']) + '/'	
		try:
			post_obj = Post.objects.get(id = post['id'])
		except:
			post_obj = Post.objects.create(id = post['id'], text=post['text'], url=url, comments=post['comments']['count'],
										likes=post['likes']['count'], reposts=post['reposts']['count'],
										views=post['views']['count'], group=group)

#Внезапно перестал работать
#def create_posts(slug):
#	p = get_posts(slug)
#	group = Group.objects.get_or_create(slug=slug)[0]
#	posts = Post.objects.filter(group=group)
#	print('OK')
#	for i in range(1, 100):
#		post = p[i]
#		print(post)
#		url = dom + slug +'?w=wall' + str(post['from_id']) + '_' + str(post['id']) + '/'	
#		
#		try:
#			post_obj = Post.objects.filter(num=post['id']).update(
#							comments=post['comments']['count'], likes=post['likes']['count'], 
#							reposts=post['reposts']['count'], views=post['views']['count'])
#		except:
#			post_obj = Post.objects.create(num=post['id'], text=post['text'], url=url, comments=post['comments']['count'],
#										likes=post['likes']['count'], reposts=post['reposts']['count'],
#										views=post['views']['count'], group=group)