import vk
from .models import Post, Group

login = '+79201673161'
password = 'igorvica2408'
vk_id = '6475437'
access_token = '92468fc6c769e45741d67a829351489ab8d61ebfc8bf916e3dd12599aaee0b2b8abc13f91e29aa45741d9'

dom = 'https://vk.com/'
domain = 'sociate'

#session = vk.AuthSession(app_id=vk_id, user_login=login, user_password=password)
#def authent():
session = vk.Session(access_token=access_token)
api = vk.API(session, v='5.74')

def get_posts(slug):
	response=api.wall.get(domain=slug, count=100)
	post = response['items']
	return post

def create_posts(slug):
	p = get_posts(slug)
	group = Group.objects.get_or_create(slug=slug)[0]
	posts = Post.objects.filter(group=group)
	for i in range(1, 100):
		post = p[i]
		url = dom + domain +'?w=wall' + str(post['from_id']) + '_' + str(post['id']) + '/'	
		try:
			post_obj = Post.objects.get(text=post['text'])
		except:
			post_obj = None
		if post_obj==None:
			post_obj = Post.objects.create(text=post['text'], url=url, comments=post['comments']['count'],
										likes=post['likes']['count'], reposts=post['reposts']['count'],
										views=post['views']['count'], group=group)
