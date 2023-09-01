from typing import Any, Optional
from django.core.management.base import BaseCommand
from sem_2_1.models import Author
from datetime import date

class Command(BaseCommand):
    help = "Create author"

    def handle(self, *args, **kwargs):
        author = Author(name='Aleksander', surname='Pushkin', email= 'aspushkin@mail.ru',
                       biography= "Великий русский поэт")
        author.save()
        self.stdout.write(f'{author}')

    
