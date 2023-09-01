from django.db import models
from datetime import datetime
from random import randint

class Kisks(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(auto_now=True)

    @staticmethod
    def statistic(n: int):
        reshka = 0
        orel = 0
        for _ in range(n):
            kick = Kisks(result=randint(0,1))
            if kick.result:
                reshka += 1
            else:
                orel += 1
        result_dict = {
            'opeл': orel, 
            'решка': reshka,
        }
        return result_dict


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_data = models.DateField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    caterory = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField(default=False)

