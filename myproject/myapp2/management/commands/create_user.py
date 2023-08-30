from typing import Any, Optional
from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        #user = User(name= 'John', email= 'John85@yandex.ru', password= 'secret', age= 25)
        #user = User(name='Neo', email='neo@example.com', password='secret',age=58)
        user = User(name='Jack', email='capinat@example.com', password='secret',age=60)
        user.save()
        self.stdout.write(f'{user}')
    