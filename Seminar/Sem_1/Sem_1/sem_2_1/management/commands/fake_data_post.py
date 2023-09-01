from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from sem_2_1.models import Post, Author
from random import randint


class Command(BaseCommand):
    help = "Create fake post"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Post_Id")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for author in Author.objects.all():
            for i in range(count +1):
                post = Post(title = f'title_{i}',
                    content = "Bla - bla - bla",
                    author = author,
                    caterory = f'caterory_{i}')
                post.save()
            




