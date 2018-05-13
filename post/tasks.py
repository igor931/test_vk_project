from vk_project.celery import app
from post.utils import create_posts 
#from __future__ import absolute_import, unicode_literals
#import random
#from celery.decorators import task

@app.task
def test(slug):
	create_posts(slug)

#@task(name="sum_two_numbers")
#def add(x, y):
#    return x + y

#@task(name="multiply_two_numbers")
#def mul(x, y):
#    total = x * (y * random.randint(3, 100))
#    return total

#@task(name="sum_list_numbers")
#def xsum(numbers):
#    return sum(numbers) 