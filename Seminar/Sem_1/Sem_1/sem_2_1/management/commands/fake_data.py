from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from sem_2_1.models import Author
from datetime import datetime

class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Author_ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in  range(count + 1):
            author = Author(name = f'name_{i}', surname = f'surname_{i}', email = f'email_{i}@ya,ru', \
                            biography="Bla_bla_bal.....")
            author.save()