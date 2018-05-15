from vk_project.celery import app
from post.utils import create_posts 


@app.task
def test(slug):
	create_posts(slug)

