import vk
from .models import Post, Group, Report
from django.utils import timezone


login = '+79201673161'
password = 'igorvica2408'
vk_id = '6475437'
access_token = 'ad135b2e8110a790e429faef6c7a86477fd985f9f9a32564be386b78f7352722727b167eebce18bfe2680'

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
	report = Report.objects.create()
	report.group = group
	for i in range(0, 100):
		post = p[i]
		url = dom + slug +'?w=wall' + str(post['from_id']) + '_' + str(post['id']) + '/'
		try:
			views = post['views']['count']
		except:
			views = None	
		defaults={'text': post['text'], 'url':url, 'group':group,
					'comments':post['comments']['count'], 'likes':post['likes']['count'], 
					'reposts':post['reposts']['count'],	'views':views}
		
		post_obj, created = Post.objects.update_or_create(
					num=post['id'],
					defaults=defaults,
		)
		
		report.text += 'Группа: {}. Комментарии: {}. Лайк: {}. Репост: {}. Просмотров: {}. Текст: {}\n'.format(group,
					post['comments']['count'], post['likes']['count'], 
					post['reposts']['count'], views, post['text'])
	report.save()